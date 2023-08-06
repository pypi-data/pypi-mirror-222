import click
from typing import *
import os
import json
from e2eqavn import __version__
from e2eqavn.utils.io import load_yaml_file
from e2eqavn.documents import Corpus
from e2eqavn.datasets import *
from e2eqavn.processor import RetrievalGeneration
from e2eqavn.keywords import *
from e2eqavn.utils.calculate import *
from e2eqavn.retrieval import *
from e2eqavn.mrc import *
from e2eqavn.evaluate import *
from e2eqavn.utils.calculate import make_input_for_retrieval_evaluator
from e2eqavn.pipeline import E2EQuestionAnsweringPipeline
import pprint
from datasets import load_metric

logger = logging.getLogger(__name__)


@click.group()
def entry_point():
    print(f"e2eqa version {__version__}")
    pass


@click.command()
def version():
    print(__version__)


@click.command()
@click.option(
    '--config', '-c',
    required=True,
    default='config/config.yaml',
    help='Path config model'
)
def train(config: Union[str, Text]):
    config_pipeline = load_yaml_file(config)
    try:
        train_corpus = Corpus.parser_uit_squad(
            config_pipeline[DATA][PATH_TRAIN],
            **config_pipeline.get(CONFIG_DATA, {})
        )
    except:
        train_corpus = Corpus.init_corpus(
            config_pipeline[DATA][PATH_TRAIN],
            **config_pipeline.get(CONFIG_DATA, {})
        )
    retrieval_config = config_pipeline.get(RETRIEVAL, None)
    reader_config = config_pipeline.get(READER, None)
    if retrieval_config.get(IS_TRAIN, False):
        retrieval_sample = RetrievalGeneration.generate_sampling(train_corpus, **retrieval_config[PARAMETERS])
        train_dataset = TripletDataset.load_from_retrieval_sampling(retrieval_sample=retrieval_sample)
        dev_evaluator = make_vnsquad_retrieval_evaluator(
            path_data_json=config_pipeline[DATA][PATH_EVALUATOR]
        )

        retrieval_learner = SentenceBertLearner.from_pretrained(
            model_name_or_path=retrieval_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/vn-sentence-embedding')
        )
        retrieval_learner.train(
            train_dataset=train_dataset,
            dev_evaluator=dev_evaluator,
            **retrieval_config[MODEL]
        )

    if reader_config.get(IS_TRAIN, False):
        try:
            eval_corpus = Corpus.parser_uit_squad(
                config_pipeline[DATA][PATH_EVALUATOR],
                **config_pipeline.get(CONFIG_DATA, {})
            )
        except:
            eval_corpus = Corpus.init_corpus(
                config_pipeline[DATA][PATH_EVALUATOR],
                **config_pipeline.get(CONFIG_DATA, {})
            )

        mrc_dataset = MRCDataset.init_mrc_dataset(
            corpus_train=train_corpus,
            corpus_eval=eval_corpus,
            model_name_or_path=reader_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/mrc_testing'),
            max_length=reader_config[MODEL].get(MAX_LENGTH, 368),
            **reader_config.get(DATA_ARGUMENT, {})
        )
        reader_model = MRCReader.from_pretrained(
            model_name_or_path=reader_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/mrc_testing'),
            lambda_weight=reader_config.get(DATA_ARGUMENT, {}).get(LAMBDA_WEIGHT, 0.6)
        )
        reader_model.init_trainer(mrc_dataset=mrc_dataset, **reader_config[MODEL])
        reader_model.train()


@click.command()
@click.option(
    '--config', '-c',
    required=True,
    default='config/config.yaml',
    help='Path config model'
)
@click.option(
    '--top_k_bm25',
    default=10,
    help='Top k retrieval by BM25 algorithm'
)
@click.option(
    '--top_k_sbert',
    default=3,
    help='Top k retrieval by sentence-bert algorithm'
)
@click.option(
    '--logging_result_pipeline',
    default=True,
    help='Logging result predict to file'
)
@click.option(
    '--path_save_log',
    default='log',
    help='Path folder for save pipeline result'
)
@click.argument('mode', default='retrieval')
def evaluate(config: Union[str, Text], mode,
             top_k_bm25: int,
             logging_result_pipeline: bool,
             path_save_log: str,
             top_k_sbert: int
             ):
    config_pipeline = load_yaml_file(config)
    retrieval_config = config_pipeline.get(RETRIEVAL, None)
    reader_config = config_pipeline.get(READER, None)
    pipeline = E2EQuestionAnsweringPipeline()

    try:
        eval_corpus = Corpus.parser_uit_squad(
            config_pipeline[DATA][PATH_EVALUATOR],
            **config_pipeline.get(CONFIG_DATA, {})
        )
    except:
        eval_corpus = Corpus.init_corpus(
            config_pipeline[DATA][PATH_EVALUATOR],
            **config_pipeline.get(CONFIG_DATA, {})
        )
    if mode in ['retrieval', 'pipeline', 'bm25']:
        logger.info("Start loading BM25")
        bm25_retrieval = BM25Retrieval(corpus=eval_corpus)
        pipeline.add_component(
            component=bm25_retrieval,
            name_component='bm25_retrieval'
        )

    context_copurs = {doc.document_id: doc.document_context for doc in eval_corpus.list_document}
    queries = {}
    relevant_docs = {}
    for doc in eval_corpus.list_document:
        if len(doc.list_pair_question_answers) == 0:
            continue
        for question_answer in doc.list_pair_question_answers:
            ques_id = hashlib.sha1(str(question_answer.question).encode('utf-8')).hexdigest()
            queries[ques_id] = question_answer.question
            if ques_id not in relevant_docs:
                relevant_docs[ques_id] = set()
            relevant_docs[ques_id].add(doc.document_id)

    if mode in ['retrieval', 'pipeline'] and retrieval_config:
        logger.info("Start loading Sbert")
        retrieval_model = SBertRetrieval.from_pretrained(retrieval_config[MODEL][MODEL_NAME_OR_PATH])
        retrieval_model.update_embedding(eval_corpus)
        pipeline.add_component(
            component=retrieval_model,
            name_component='sbert_retrieval'
        )

    if mode in ['retrieval', 'bm25']:
        logger.info("Start evaluate retrieval")
        information_evaluator = InformationRetrievalEvaluatorCustom(
            queries=queries,
            corpus=context_copurs,
            relevant_docs=relevant_docs
        )
        information_evaluator.compute_metrices_retrieval(
            pipeline=pipeline
        )

    if mode in ['reader', 'pipeline'] and reader_config:
        logger.info("Start loading Reader")
        mrc_dataset = MRCDataset.init_mrc_dataset(
            corpus_eval=eval_corpus,
            model_name_or_path=reader_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/mrc_dev'),
            max_length=reader_config[MODEL].get(MAX_LENGTH, 368)
        )
        reader_model = MRCReader.from_pretrained(
            model_name_or_path=reader_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/mrc_dev')
        )
        if mode == 'reader':
            logger.info("Start evaluate reader")
            reader_model.init_trainer(mrc_dataset=mrc_dataset, **reader_config[MODEL])
            reader_model.evaluate(mrc_dataset.evaluator_dataset)
        elif mode == 'pipeline':
            pipeline.add_component(
                component=reader_model,
                name_component='reader'
            )

    if mode == 'pipeline':
        logger.info("Start evaluate pipeline")
        metric_fn = load_metric('squad')
        predictions, ground_truth, list_questions = [], [], []
        ground_truth = []
        idx = 0
        for doc in eval_corpus.list_document:
            for pair_ques_ans in doc.list_pair_question_answers:
                question = pair_ques_ans.question
                list_questions.append(question)
                answers = [ans[eval_corpus.answer_key] for ans in pair_ques_ans.list_dict_answer]
                ground_truth.append(
                    {
                        'answers': {'text': answers},
                        'id': str(idx)
                    }
                )
                idx += 1
        pred_answers = pipeline.run(
            queries=list_questions,
            top_k_bm25=top_k_bm25,
            top_k_sbert=top_k_sbert,
            top_k_qa=1
        )
        if logging_result_pipeline:
            results_logging = []
        for idx, ans_pred in enumerate(pred_answers['answer']):
            predictions.append(
                {'prediction_text': ans_pred[0].get('answer', ""), 'id': str(idx)}
            )
            ground_truth[idx]['answers']['answer_start'] = [ans_pred[0]['answer_start_idx']] * len(
                ground_truth[idx]['answers']['text'])
            if logging_result_pipeline:
                results_logging.append({
                    'question': list_questions[idx],
                    'answer_pred': ans_pred[0].get('answer', ""),
                    'answer_truth': ground_truth[idx],
                    'logging': [
                        {
                            'doc': doc_retrieval.document_context,
                            'bm25_score': doc_retrieval.bm25_score,
                            'score_start': doc_reader.get('score_start', 0),
                            'score_end': doc_reader.get('score_end', 0),
                            'reader_score': doc_reader.get('score', 0),
                            'answer_start_idx': doc_reader.get('answer_start_idx', 0),
                            'answer_end_idx': doc_reader.get('answer_end_idx', 0)
                        } for doc_retrieval, doc_reader in
                        zip(pred_answers['documents'][idx], pred_answers['reader_logging'][idx])
                    ]
                }
                )
        if logging_result_pipeline:
            write_json_file(results_logging, os.path.join(path_save_log, 'logging.json'))
        logger.info(f"Evaluate E2E pipeline: {metric_fn.compute(predictions=predictions, references=ground_truth)}")


@click.command()
@click.option(
    '--config', '-c',
    required=True,
    help='Path config model'
)
@click.option(
    '--question', '-q',
    required=True,
)
@click.option(
    '--top_k_bm25',
    default=10,
    help='Top k retrieval by BM25 algorithm'
)
@click.option(
    '--top_k_sbert',
    default=3,
    help='Top k retrieval by sentence-bert algorithm'
)
@click.option(
    '--top_k_qa',
    default=1,
    help='Top k retrieval by sentence-bert algorithm'
)
@click.argument('mode', default='retrieval')
def test(config: Union[str, Text], question: str, top_k_bm25: int, top_k_sbert: int, top_k_qa: int, mode: str):
    config_pipeline = load_yaml_file(config)
    retrieval_config = config_pipeline.get(RETRIEVAL, None)
    reader_config = config_pipeline.get(READER, None)
    pipeline = E2EQuestionAnsweringPipeline()
    corpus = Corpus.parser_uit_squad(
        config_pipeline[DATA][PATH_TRAIN],
        **config_pipeline.get(CONFIG_DATA, {})
    )
    if mode in ['retrieval', 'pipeline'] and retrieval_config:
        bm25_retrieval = BM25Retrieval(corpus=corpus)
        pipeline.add_component(
            component=bm25_retrieval,
            name_component='retrieval_1'
        )
        retrieval_model = SBertRetrieval.from_pretrained(retrieval_config[MODEL][MODEL_NAME_OR_PATH])
        retrieval_model.update_embedding(corpus=corpus)
        pipeline.add_component(
            component=retrieval_model,
            name_component='retrieval_2'
        )

    if mode in ['reader', 'pipeline'] and reader_config:
        reader_model = MRCReader.from_pretrained(
            model_name_or_path=reader_config[MODEL].get(MODEL_NAME_OR_PATH, 'khanhbk20/mrc_dev')
        )
        pipeline.add_component(
            component=reader_model,
            name_component='reader'
        )
    output = pipeline.run(
        queries=question,
        top_k_bm25=top_k_bm25,
        top_k_sbert=top_k_sbert,
        top_k_qa=top_k_qa
    )
    if 'documents' in output:
        output['documents'] = [[doc.__dict__ for doc in list_document] for list_document in output['documents']]
    pprint.pprint(
        output
    )


entry_point.add_command(version)
entry_point.add_command(train)
entry_point.add_command(evaluate)
entry_point.add_command(test)
