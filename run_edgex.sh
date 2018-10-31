#!/bin/bash

docker-compose up -d volume
docker-compose up -d portainer
docker-compose up -d consul
docker-compose up -d mongo
docker-compose up -d config-seed
docker-compose up -d logging
docker-compose up -d notifications
docker-compose up -d rulesengine
docker-compose up -d data
docker-compose up -d export-client
docker-compose up -d export-distro
docker-compose up -d metadata
docker-compose up -d scheduler
docker-compose up -d command
docker-compose up -d device-virtual
docker-compose up -d device-bacnet
