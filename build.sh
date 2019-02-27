#!/usr/bin/env bash
docker-compose build web
docker-compose build jupyter
docker-compose build test