#!/bin/bash

IMAGE_NAME="covid-19-classifier-img"
CONTAINER_NAME="covid-19-classifier"

docker build -t $IMAGE_NAME --no-cache .
docker run -dit --gpus all --name $CONTAINER_NAME -p 8888:8888 $IMAGE_NAME

while [ "$(docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME")" != "true" ]; do
    sleep 1
done

docker exec -it $CONTAINER_NAME bash