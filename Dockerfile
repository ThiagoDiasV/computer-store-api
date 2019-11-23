FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /silvertec
WORKDIR /silvertec
ADD . /silvertec/
RUN pip install -r requirements.txt