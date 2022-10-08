# syntax=docker/dockerfile:1
FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /meet2go
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /meet2go

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]