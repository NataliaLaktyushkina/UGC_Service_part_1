#!/bin/sh
set -u

echo "Waiting for Kafka..."

while ! nc -z broker 29092; do
  sleep 2
done

echo "Kafka started"


echo "Waiting for Clickhouse..."

while ! nc -z  clickhouse-node1 8123; do
  sleep 2
done

echo "Clickhouse started"

#exec "$@"
python main.py