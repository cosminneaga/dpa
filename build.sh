#!/usr/bin/env bash

# ----------------------------- COPY DATABASE ENV ---------------------------- #
ENVDB='./db/env/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./db/env/example.env $ENVDB
fi

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENVAPI='./api/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./api/example.env $ENVAPI
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
ENVBLOGGER='./blogger/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env .'"
    cp ./blogger/example.env $ENVBLOGGER
fi

# echo "DELETING ./blogger/node_modules... PLEASE WAIT"
# rm -r ./blogger/node_modules

# rm ./blogger/package-lock.json

docker compose up -d --build