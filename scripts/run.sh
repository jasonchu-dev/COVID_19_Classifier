#!/bin/bash

IMAGE_NAME="covid-19-classifier-img"

if docker inspect "$IMAGE_NAME" &> /dev/null; then
    echo "The image $IMAGE_NAME exists."
    docker start covid-19-classifier-container
else
    echo "The image $IMAGE_NAME does not exist."
    docker build -t covid-19-classifier-img .
    docker run -d --name covid-19-classifier-container covid-19-classifier-img
fi