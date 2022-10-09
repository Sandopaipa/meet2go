FROM python:latest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /meet2go
COPY requirements.txt /meet2go/requirements.txt
RUN pip install -r requirements.txt
COPY . /meet2go
