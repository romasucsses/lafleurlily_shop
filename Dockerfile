# Stage 1: Build Vue.js Projects

# Build Stage for Vue Lily
FROM node:22-alpine3.19 as build-lily
WORKDIR /vue_lily
COPY vue_lily/package*.json ./
RUN npm install
COPY vue_lily ./
RUN npm run build

# Build Stage for Vue DA
FROM node:22-alpine3.19 as build-da
WORKDIR /vue_da
COPY vue_da/package*.json ./
RUN npm install
COPY vue_da ./
RUN npm run build

# Build Stage for Vue Bastina
FROM node:22-alpine3.19 as build-bastina
WORKDIR /vue_bastina
COPY vue_bastina/package*.json ./
RUN npm install
COPY vue_bastina ./
RUN npm run build

# Stage 2: Serve Built Files Using Nginx
FROM nginx:1.26-alpine as production

# Install Certbot for SSL
RUN apk update && \
    apk add --no-cache certbot certbot-nginx

# Create directories for Certbot challenges
RUN mkdir -p /var/www/certbot

# Copy custom Nginx configuration files
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/conf.d /etc/nginx/conf.d

# Copy built files from each project
COPY --from=build-lily /vue_lily/dist /usr/share/nginx/html/lily
COPY --from=build-da /vue_da/dist /usr/share/nginx/html/da
COPY --from=build-bastina /vue_bastina/dist /usr/share/nginx/html/bastina

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
