FROM python:3.12.6

WORKDIR /app/backend

# pydubのインストール
# RUN apt-get update && apt-get install -y libasound-dev ffmpeg && apt-get clean



RUN apt-get update && \apt-get install -y pulseaudio
RUN pip install --no-cache-dir poetry==1.7.1

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi 

# pygame を直接インストール
RUN pip install pygame

COPY . /

WORKDIR /app

# エントリーポイントスクリプトを実行
CMD ["./backend/entrypoint.sh"]
