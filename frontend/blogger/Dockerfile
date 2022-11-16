FROM node:18

ADD . /frontend
WORKDIR /frontend

RUN npm install
RUN npm run build
CMD npm run preview