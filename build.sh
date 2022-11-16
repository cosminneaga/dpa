#!/usr/bin/env bash

# ----------------------------- COPY BACKEND ENV ----------------------------- #
ENV='./backend/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./backend/example.env $ENV
fi

# ------------------------- COPY BLOGGER FRONTEND ENV ------------------------ #
ENV='./frontend/blogger/.env'
if [ ! -f $ENV ]; then
    echo "File $ENV does not exist, copying 'example.env.'"
    cp ./frontend/blogger/example.env $ENV
fi

docker compose up -d --build