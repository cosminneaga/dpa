#!/usr/bin/env bash

# ----------------------------- COPY BACKEND ENV ----------------------------- #
FILE1='./api/.env'
if [ ! -f $FILE1 ]; then
    echo "File $FILE1 does not exist, copying 'example.env .'"
    cp ./api/example.env $FILE1
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
FILE2='./blogger/.env'
if [ ! -f $FILE2 ]; then
    echo "File $FILE2 does not exist, copying 'example.env .'"
    cp ./blogger/example.env $FILE2
fi

# ----------------------------- COPY DATABASE ENV ---------------------------- #
FILE3='./db/.env'
if [ ! -f $FILE3 ]; then
    echo "File $FILE3 does not exist, copying 'example.env .'"
    cp ./db/example.env $FILE3
fi

# echo "DELETING ./blogger/node_modules... PLEASE WAIT"
# rm -r ./blogger/node_modules

# rm ./blogger/package-lock.json

docker compose up -d --build