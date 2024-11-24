# Use official Nginx image as the base image
FROM nginx:alpine

# Copy the frontend files (index.html, and other assets if needed) into the default Nginx directory
COPY ./ /usr/share/nginx/html/

# Expose port 80 (default for HTTP)
EXPOSE 80
