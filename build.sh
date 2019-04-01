#!/usr/bin/env bash
docker-compose build jupyter
docker-compose build web

docker-compose -f docker-compose.test.yml build test