FROM node:18-slim

ADD . /frontend/blogger
WORKDIR /frontend/blogger

RUN npm install
RUN npm run build
CMD npm run preview