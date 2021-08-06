FROM python:3.8.6-alpine3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements/base.txt .
RUN pip install -r base.txt

COPY .. .