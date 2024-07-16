"""SPARQL/FastAPI utils."""

from collections.abc import Iterable, Iterator, Mapping
from typing import cast

from SPARQLWrapper import QueryResult
from sparql_api.models.document_model import CorpusInfo, DocumentModel
from toolz import valmap


def get_bindings(query_result: QueryResult) -> Iterator[dict]:
    query_json = cast(Mapping, query_result.convert())
    bindings = map(
        lambda binding: valmap(lambda v: v["value"], binding),
        query_json["results"]["bindings"],
    )

    return bindings


def get_document_models(bindings: Iterable[dict[str, str]]) -> Iterator[DocumentModel]:
    for binding in bindings:
        model = DocumentModel(
            document_uri=binding["document_uri"],
            document_label=binding["document_label"],
            corpus_info=CorpusInfo(
                corpus_uri=binding["corpus_uri"], corpus_label=binding["corpus_label"]
            ),
        )

        yield model
