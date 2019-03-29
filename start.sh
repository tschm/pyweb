#!/usr/bin/env bash
echo "http://localhost:4445/admin"
docker-compose run -p "4445:8000" web #python /pyweb/start.py

