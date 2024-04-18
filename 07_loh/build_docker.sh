#!/bin/bash

# Build Docker image
docker build -t loh-predictor .

# Check if the image was built successfully
if [ $? -eq 0 ]; then
    echo "Docker image built successfully."
else
    echo "Error: Failed to build Docker image."
fi
