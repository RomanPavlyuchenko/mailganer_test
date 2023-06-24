FROM python:2.7.18-slim

RUN mkdir /mailsender && apt-get update && apt-get install -y libpq-dev postgresql-client netcat
WORKDIR /mailsender

COPY ./requirements.txt /mailsender/

RUN pip install -r requirements.txt

COPY ./mailsender /mailsender
RUN chmod +x /mailsender/entrypoint.sh
