# FROM python:3.12-slim
FROM --platform=linux/amd64 python:3.12-slim

WORKDIR /app
COPY ./app /app
ENV PYTHONPATH /app/src

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

CMD ["python3", "src/main.py"]