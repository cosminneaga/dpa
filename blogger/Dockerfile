FROM node:18-alpine

WORKDIR /app
COPY . .
RUN apk add bash
RUN npm install
RUN npm run build

EXPOSE 1000

CMD npm run preview