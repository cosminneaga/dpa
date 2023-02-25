#!/usr/bin/env bash

rm /etc/nginx/nginx.conf
cp /root/dpa/server/nginx.conf /etc/nginx/nginx.conf
certbot --nginx