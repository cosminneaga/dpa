#!/usr/bin/env bash

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENV='./backend/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./backend/example.env $ENV
fi

# ------------------------- COPY BLOGGER ENV ------------------------ #
ENV='./blogger/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./blogger/example.env $ENV
fi

echo "DELETING ./blogger/node_modules... PLEASE WAIT"
rm -r ./blogger/node_modules

docker compose up -d --build

cd ./blogger
npm install
npm run dev