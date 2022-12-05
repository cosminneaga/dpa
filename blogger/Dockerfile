# FROM node:18.12.1-alpine3.15 AS base

# COPY . /blogger/
# WORKDIR /blogger


# FROM base AS dependencies
# RUN npm install
# RUN npm run build


# FROM base AS release
# COPY --from=dependencies /blogger/node_modules ./node_modules
# COPY . .
# CMD npm run preview -- --port=3000




FROM node:18.12.1-alpine3.15

WORKDIR /app
# RUN chown node:node ./
COPY . .
RUN npm install
RUN npm run build
CMD npm run preview -- --port=3000




# build stage
# FROM node:lts-alpine as build-stage
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]