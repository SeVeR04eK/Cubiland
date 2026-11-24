# Frontend Dockerfile - DEFERRED
#
# This Dockerfile is deferred until the frontend application has:
# - A valid build script (npm run build)
# - Vite or another build tool configured
# - Production build output directory (dist/)
#
# Current package.json has dependencies but no build scripts.
# This file will be updated when frontend development begins.
#
# For reference, the intended multi-stage build will be:
# FROM node:20-slim AS build
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build
#
# FROM nginx:alpine
# COPY --from=build /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
