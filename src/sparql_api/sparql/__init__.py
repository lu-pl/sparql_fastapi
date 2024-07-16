from importlib.resources import files
from types import SimpleNamespace


_sparql_dir = files("sparql_api") / "sparql"
queries = SimpleNamespace()

for _query in _sparql_dir.rglob("*.rq"):
    with open(_query) as f:
        query = f.read()

    setattr(queries, _query.stem, query)
