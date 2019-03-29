#!/usr/bin/env bash
docker-compose build --no-cache test
docker-compose run test
#docker-compose -f docker-compose.test.yml run test npm test
