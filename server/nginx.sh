#!/usr/bin/env bash

rm /etc/nginx/nginx.conf
cp /dpa/server/nginx.conf /etc/nginx/nginx.conf
certbot --nginx