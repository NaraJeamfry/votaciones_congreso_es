FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:/app:/app/votaciones_congreso

WORKDIR /app

ARG environment=narajeamfry

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev

COPY ./requirements/* /app/requirements/
RUN pip install -r requirements/$environment.txt

RUN apk del .tmp
