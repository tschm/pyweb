#!/usr/bin/env bash
echo "http://localhost:4445"
docker-compose run -p "4445:8000" jupyter python /pyweb/start.py

