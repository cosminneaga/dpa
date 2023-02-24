FROM node:18-alpine

RUN apk add bash

WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm install
COPY . .
RUN npm run build

EXPOSE 1000

CMD npm run preview