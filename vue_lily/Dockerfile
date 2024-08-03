FROM node:22-alpine3.19 as builder

WORKDIR /vue_lily

COPY . .
COPY package*.json ./

RUN npm install
RUN npm run build

# Stage 2: Serve Vue.js files using Nginx
FROM nginx:1.26-alpine as production

RUN apk update && \
    apk add --no-cache certbot certbot-nginx
# Create directories for Certbot
RUN mkdir -p /var/www/certbot

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/conf.d /etc/nginx/conf.d
COPY --from=builder /vue_lily/dist /usr/share/nginx/html

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
