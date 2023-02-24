#!/usr/bin/env bash

rm /etc/nginx/nginx.conf
cp /server/nginx.conf /etc/nginx/nginx.conf
certbot --nginx