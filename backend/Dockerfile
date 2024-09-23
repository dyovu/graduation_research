FROM python:3.10.12-slim

WORKDIR /app

# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir poetry==1.7.1

COPY pyproject.toml poetry.lock* /app/


RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


COPY . /app/backend

# エントリーポイントスクリプトを実行
CMD ["./backend/entrypoint.sh"]
