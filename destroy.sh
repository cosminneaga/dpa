#!/usr/bin/env bash

docker compose down --volumes --remove-orphans
docker rmi dpa-backend dpa-blogger