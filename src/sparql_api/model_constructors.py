"""Model constructors for use in SPARQLAdapter"""

from SPARQLWrapper import QueryResult
from sparql_api.models.document_model import DocumentModel
from sparql_api.utils.utils import get_bindings, get_document_models


def get_documents_constructor(query_result: QueryResult) -> list[DocumentModel]:
    bindings = get_bindings(query_result)
    models: list[DocumentModel] = list(get_document_models(bindings))

    return models
