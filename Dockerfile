FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD Pipfile .
ADD Pipfile.lock .

RUN pip install pipenv && pipenv install
COPY . /app

EXPOSE 5000
