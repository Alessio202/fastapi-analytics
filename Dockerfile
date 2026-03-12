FROM python:3.12-slim

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction 
COPY . .

ENV PYTHONPATH=/code/src

EXPOSE 8000

CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8000"]