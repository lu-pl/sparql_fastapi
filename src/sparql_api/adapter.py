"""SPARQLAdapter."""

from SPARQLWrapper import SPARQLWrapper, QueryResult
from pydantic import BaseModel
from collections.abc import Callable


class SPARQLAdapter:
    """SPARQL Adapter for QueryResult to Pydantic model conversions."""

    def __init__(self, sparql_wrapper: SPARQLWrapper):
        self.sparql_wrapper = sparql_wrapper

    def __call__[
        ModelType: BaseModel
    ](
        self, query: str, model_constructor: Callable[[QueryResult], ModelType]
    ) -> ModelType:
        """Execute query using sparql_wrapper and pass the result to model_constructor.

        model_constructor is responsible for instantiating a Pydantic model.
        """
        self.sparql_wrapper.setQuery(query)

        query_result = self.sparql_wrapper.query()
        model = model_constructor(query_result)

        return model
