FROM python:3.9.6-slim-buster

WORKDIR /usr/src/

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
# pycファイルが生成されなくなる
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  # ubuntuのキャッシュされたパッケージファイルを削除する
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .