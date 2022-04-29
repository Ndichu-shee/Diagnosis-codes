FROM python:3.8

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image

ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app

ADD . /app


RUN pip install -r requirements.txt



COPY . /app

