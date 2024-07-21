"""SPARQL API tinkering."""

import os
from string import Template

from SPARQLWrapper import JSON, SPARQLWrapper
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi_pagination import add_pagination, paginate
from fastapi_pagination.links import Page
from sparql_api.adapter import SPARQLAdapter
from sparql_api.model_constructors import get_documents_constructor
from sparql_api.models import DocumentModel
from sparql_api.sparql import queries


load_dotenv()


app = FastAPI()

# sparql = SPARQLWrapper("https://triplestore.acdh-dev.oeaw.ac.at/clscor/sparql")
# sparql.setCredentials("clscor", os.getenv("password"))

sparql = SPARQLWrapper("https://clscor.acdh-dev.oeaw.ac.at/sparql")
sparql.setReturnFormat(JSON)

adapter = SPARQLAdapter(sparql_wrapper=sparql)


@app.get("/documents")
def get_documents() -> Page[DocumentModel]:
    models = adapter(
        query=queries.corpus_documents, model_constructor=get_documents_constructor
    )

    return paginate(models)


@app.get("/documents/entity/{document_id}")
def get_document_by_id(document_id: str) -> DocumentModel:
    query_template = Template(queries.corpus_document_by_id)
    query = query_template.substitute(document_id=document_id)

    models = adapter(query=query, model_constructor=get_documents_constructor)

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

    models = adapter(query=query, model_constructor=get_documents_constructor)

    return models


add_pagination(app)
