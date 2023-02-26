FROM python:3.8.16-slim

RUN apt-get install bash

WORKDIR /processor
COPY requirements.txt .
# RUN pip install 'Flask==2.1.2'
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD if [ "$APP_ENV" = "production" ] ; then gunicorn --bind 0.0.0.0:9000 app:app ; else python app.py ; fi