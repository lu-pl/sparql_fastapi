# sparql-fastapi tinkering

## Requirements

* Python >= 3.12

## Installation

### Container
Build an image and run it:

```shell
git clone https://github.com/lu-pl/sparql_fastapi.git
cd sparql_fastapi

docker build . -t sparql-fastapi
docker run -p 80:80 sparql-fastapi 
```

### Source
Activate a virtual environment and run:

```shell
git clone https://github.com/lu-pl/sparql_fastapi.git
cd sparql_fastapi

pip install .

fastapi dev src/sparql_api/main.py
```
