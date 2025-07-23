#!/bin/bash
#
echo "building docker_image"
docker build -t web .

echo "running docker container"
docker run -p 5000:5000 web
