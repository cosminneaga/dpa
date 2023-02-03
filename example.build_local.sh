#!/usr/bin/env bash

bash build.sh

echo "LOCAL BUILD FILE IS BEING RUNNED"

# run extra commands needed after build on your local

# production
## docker system prune --all -f

# local_pc
## cd ./blogger
## npm install
## npm run dev


### USAGE ###
# cp example.build_local.sh build_local.sh
# bash build_local.sh