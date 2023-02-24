FROM python:3.8-alpine

RUN apk update && apk upgrade
RUN apk add bash

WORKDIR /api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD if [ "$APP_ENV" = "production" ] ; then gunicorn --bind 0.0.0.0:8080 app:app ; else python app.py ; fi