FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /exercise_tracker/

RUN pip install pipenv

COPY . .

RUN pipenv install