from mock.mock_decision import get_mock_decision_result, get_mock_event, get_mock_paths
from models.graphrag_infer import infer_decision_with_graphrag


def get_decision_payload(use_mock: bool = True) -> dict:
    if use_mock:
        return {
            "event": get_mock_event(),
            "paths": get_mock_paths(),
            "decision": get_mock_decision_result(),
        }
    return infer_decision_with_graphrag()
