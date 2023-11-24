#!/bin/bash

IMAGE_NAME="covid-19-classifier-img"
CONTAINER_NAME="covid-19-classifier-container"

docker build -t $IMAGE_NAME --no-cache .
docker run -dit --name $CONTAINER_NAME -p 8888:8888 $IMAGE_NAME
# docker run -dit --name $CONTAINER_NAME $IMAGE_NAME

while [ "$(docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME")" != "true" ]; do
    sleep 1
done

# docker run -p 8888:8888 $IMAGE_NAME
docker exec -it $CONTAINER_NAME bash