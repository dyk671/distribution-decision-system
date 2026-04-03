from mock.mock_qa import EXAMPLE_QA, mock_answer
from models.llm_infer import infer_with_llm


def get_example_questions() -> list[str]:
    return list(EXAMPLE_QA.keys())


def answer_question(question: str, use_mock: bool = True) -> dict:
    if use_mock:
        return mock_answer(question)
    return infer_with_llm(question)
