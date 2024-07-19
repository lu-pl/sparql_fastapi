FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install .
EXPOSE 80
CMD ["fastapi", "run", "src/sparql_api/main.py", "--port", "80"]
