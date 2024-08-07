# Use an official base image
FROM ubuntu:latest

# Create a directory inside the container
RUN mkdir -p /app

# Copy the file from the host to the container
COPY /var/lib/docker/volumes/my-vol/_data /app/new_folder

# Set the working directory
WORKDIR /app
