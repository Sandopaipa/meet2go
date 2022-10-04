# syntax=docker/dockerfile:1
FROM python:lastest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /meet2go
COPY requiremenets.txt /meet2go/
RUN pip install -r requiremenets.txt
COPY . /meet2go/