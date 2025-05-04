#!/bin/sh

set -x

# Stop and remove any existing container named carbon-app-container
if docker ps -a --format '{{.Names}}' | grep -q '^carbon-app-container$'; then
  echo "Stopping and removing existing container..."
  docker stop carbon-app-container
  docker rm carbon-app-container
fi

# Rebuild the image
echo "Building the Docker image..."
docker build -t carbon-app .

# Run the container with port mapping and a fixed name
echo "Running the Docker container..."
docker run -d -p 5000:5000 --name carbon-app-container carbon-app