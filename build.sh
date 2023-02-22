#!/usr/bin/env bash

# ----------------------------- COPY DATABASE ENV ---------------------------- #
ENV='./db/env/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./db/env/example.env $ENV
fi

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENV='./api/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./api/example.env $ENV
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
ENV='./blogger/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./blogger/example.env $ENV
fi

# echo "DELETING ./blogger/node_modules... PLEASE WAIT"
# rm -r ./blogger/node_modules

# rm ./blogger/package-lock.json

docker compose up -d --build