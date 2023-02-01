# FROM ubuntu:20.04

# ADD . /backend
# WORKDIR /backend

# RUN apt-get update && apt-get install -y \
#   nano \
#   python3.6 \
#   python3-pip

# RUN pip3 install -r requirements.txt 
# CMD python3 -u app.py


FROM python:3

WORKDIR /api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD python app.py