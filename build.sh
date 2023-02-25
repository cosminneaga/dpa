#!/usr/bin/env bash

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENV='./api/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./api/example.env ./api/.env
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
ENV='./blogger/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./blogger/example.env ./blogger/.env
fi

# ------------------------- COPY DB ENV ------------------------ #
ENV='./db/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./db/example.env ./db/.env
fi

# ------------------------- COPY PROCCESSOR ENV ------------------------ #
ENV='./proccessor/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./proccessor/example.env ./proccessor/.env
fi

docker compose up -d --build