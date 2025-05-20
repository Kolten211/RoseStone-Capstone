FROM python:3.9.18-alpine3.18

RUN apk add build-base

RUN apk add postgresql-dev gcc python3-dev musl-dev

ARG FLASK_APP
ARG FLASK_ENV
ARG DATABASE_URL
ARG SCHEMA
ARG SECRET_KEY
ARG S3_BUCKET
ARG S3_KEY
ARG S3_SECRET

ENV FLASK_APP=$FLASK_APP
ENV FLASK_ENV=$FLASK_ENV
ENV DATABASE_URL=$DATABASE_URL
ENV SCHEMA=$SCHEMA
ENV SECRET_KEY=$SECRET_KEY
ENV S3_BUCKET=$S3_BUCKET
ENV S3_KEY=$S3_KEY
ENV S3_SECRET=$S3_SECRET

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY . .

RUN flask db upgrade
RUN flask seed all
CMD gunicorn app:app