"""SPARQL API tinkering."""

from string import Template

from SPARQLWrapper import JSON, SPARQLWrapper
from fastapi import FastAPI, HTTPException
from fastapi_pagination import add_pagination, paginate
from fastapi_pagination.links import Page
from sparql_api.adapter import SPARQLModelAdapter
from sparql_api.models import DocumentModel
from sparql_api.sparql import queries


app = FastAPI()

sparql = SPARQLWrapper("https://clscor.acdh-dev.oeaw.ac.at/sparql")
# sparql.setReturnFormat(JSON)

adapter = SPARQLModelAdapter(sparql_wrapper=sparql)


@app.get("/documents")
def get_documents() -> Page[DocumentModel]:
    models = adapter(query=queries.corpus_documents, model_constructor=DocumentModel)

    return paginate(models)


@app.get("/documents/entity/{document_id}")
def get_document_by_id(document_id: str) -> DocumentModel:
    query_template = Template(queries.corpus_document_by_id)
    query = query_template.substitute(document_id=document_id)

    models = adapter(query=query, model_constructor=DocumentModel)

    try:
        model = models[0]
    except IndexError:
        raise HTTPException(
            status_code=404, detail=f"Item with ID '{document_id}' not found."
        )

    return model


@app.get("/documents/")
def get_document_by_name(title: str | None = None):
    query_template = Template(queries.corpus_documents_by_title)
    query = query_template.substitute(title=title)

    models = adapter(query=query, model_constructor=DocumentModel)

    return models


add_pagination(app)
