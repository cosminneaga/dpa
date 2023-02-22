#!/usr/bin/env bash

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENV='./api/.env'
if [ ! -f $ENV ]
then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./api/example.env $ENV
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
ENV='./blogger/.env'
if [ ! -f $ENV ]
then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./blogger/example.env $ENV
fi

# ------------------------- COPY DB ENV ------------------------ #
ENV='./db/.env'
if [ ! -f $ENV ]
then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./db/example.env $ENV
fi

docker compose up -d --build