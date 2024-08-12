FROM node:22-alpine3.19

WORKDIR /vue_lily

COPY . .
COPY package*.json ./

RUN npm install
RUN npm install dotenv
RUN npm run build

