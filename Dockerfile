FROM ubuntu:20.04

ADD . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
  ca-certificates \
  curl \
  git \
  nano \
  python3.6 \
  python3-pip

ARG NODE_VERSION=18.12.1
ARG NODE_PACKAGE=node-v$NODE_VERSION-linux-x64
ARG NODE_HOME=/opt/$NODE_PACKAGE

ENV NODE_PATH $NODE_HOME/lib/node_modules
ENV PATH $NODE_HOME/bin:$PATH

RUN curl https://nodejs.org/dist/v$NODE_VERSION/$NODE_PACKAGE.tar.gz | tar -xzC /opt/

RUN pip3 install -r requirements.txt 

