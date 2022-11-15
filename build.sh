#!/usr/bin/env bash

FILE='.env'
if [ -f $FILE ]; then
    echo "File $FILE exists."
else
    echo "File $FILE does not exist, copying example.env."
    cp example.env .env
fi

docker-compose up -d --build