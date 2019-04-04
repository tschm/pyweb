#!make
PROJECT_VERSION := $(shell python setup.py --version)

SHELL := /bin/bash
PACKAGE := pyweb

include .env
export


.PHONY: help build test teamcity jupyter graph doc tag server


.DEFAULT: help

help:
	@echo "make build"
	@echo "       Build the docker image."
	@echo "make test"
	@echo "       Build the docker image for testing and run them."
	@echo "make teamcity"
	@echo "       Run tests, build a dependency graph and construct the documentation."
	@echo "make jupyter"
	@echo "       Start the Jupyter server."
	@echo "make graph"
	@echo "       Build a dependency graph."
	@echo "make doc"
	@echo "       Construct the documentation."
	@echo "make tag"
	@echo "       Make a tag on Github."
	@echo "make server"
	@echo "       Start the Flask server."


build:
	docker-compose build jupyter

test:
	mkdir -p artifacts
	docker-compose -f docker-compose.test.yml build sut
	docker-compose -f docker-compose.test.yml run sut

teamcity: test graph doc

jupyter: build
	echo "http://localhost:${PORT}"
	docker-compose up jupyter

graph: test
	mkdir -p ${PWD}/artifacts/graph

	docker run --rm --mount type=bind,source=${PWD}/${PACKAGE},target=/pyan/${PACKAGE},readonly \
		   tschm/pyan:latest python pyan.py ${PACKAGE}/**/*.py -V --uses --defines --colored --dot --nested-groups > graph.dot

	# remove all the private nodes...
	grep -vE "____" graph.dot > graph2.dot

	docker run --rm -v ${PWD}/graph2.dot:/pyan/graph.dot:ro \
		   tschm/pyan:latest dot -Tsvg /pyan/graph.dot > artifacts/graph/graph.svg

	rm graph.dot graph2.dot

doc: test
	docker-compose -f docker-compose.test.yml run sut sphinx-build /source artifacts/build

tag: test
	git tag -a ${PROJECT_VERSION} -m "new tag"
	git push --tags


server:
	docker-compose run -p "4445:8000" web python start.py

