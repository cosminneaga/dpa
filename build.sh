#!/usr/bin/env bash

FILE='./backend/.env'
if [ -f $FILE ]; then
    echo "File $FILE exists."
else
    echo "File $FILE does not exist, copying example.env."
    cp ./backend/example.env ./backend/.env
fi

docker compose up -d --build