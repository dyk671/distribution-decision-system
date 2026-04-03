from mock.mock_graph import get_mock_graph
from models.neo4j_query import query_graph


def get_graph_data(use_mock: bool = True) -> dict:
    if use_mock:
        return get_mock_graph()
    return query_graph()
