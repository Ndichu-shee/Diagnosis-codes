FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /records
WORKDIR /records
ADD . /records
RUN pip install -r requirements.txt