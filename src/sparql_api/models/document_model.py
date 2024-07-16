from pydantic import BaseModel, AnyUrl


class CorpusInfo(BaseModel):
    corpus_uri: AnyUrl
    corpus_label: str


class DocumentModel(BaseModel):
    document_uri: AnyUrl
    document_label: str
    corpus_info: CorpusInfo
