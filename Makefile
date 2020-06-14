#!make
PROJECT_VERSION := $(shell python setup.py --version)

SHELL := /bin/bash
PACKAGE := pyweb


.PHONY: help build test teamcity graph doc tag server clean


.DEFAULT: help

help:
	@echo "make build"
	@echo "       Build the docker image."
	@echo "make test"
	@echo "       Build the docker image for testing and run them."
	@echo "make tag"
	@echo "       Make a tag on Github."
	@echo "make server"
	@echo "       Start the Flask server."

build:
	docker-compose build web

test:
	mkdir -p artifacts
	docker-compose -f docker-compose.test.yml run sut

tag: test
	git tag -a ${PROJECT_VERSION} -m "new tag"
	git push --tags

server: build
	docker-compose run -p "4445:8000" web python start.py

clean:
	docker-compose -f docker-compose.yml down -v --rmi all --remove-orphans
	docker-compose -f docker-compose.test.yml down -v --rmi all --remove-orphans
