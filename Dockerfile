FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/runclub

COPY ./req.txt /usr/src/req.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/runclub

EXPOSE 8000
