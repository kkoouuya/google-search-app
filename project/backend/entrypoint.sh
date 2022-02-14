#!/bin/bash

echo "waiting for mysql server"

while ! nc -z mysql 3306; do
  sleep 0.5
done

echo "Connection Successfully"

# 変数$@はシェルスクリプトの変数がすべて展開される変数
exec "$@"