FROM python:3.9.12-buster
# Базовый образ Python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./requirements.txt .

RUN apt update && apt install -y netcat && which nc

# install dependencies
RUN pip install --no-cache-dir --upgrade pip &&\
 pip install --no-cache-dir -r requirements.txt

# Copy application
COPY ./app /app

# create entrypoint for Kafka and ClickHouse waiting
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh","/app/entrypoint.sh"]
#CMD ["python", "/app/main.py"]