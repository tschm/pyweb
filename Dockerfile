FROM python:3.7.7-slim-stretch as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

# COPY this project into a local folder and install from there
COPY . /tmp/server

ARG project=server
ARG package=pyserver

ENV APPLICATION_SETTINGS="/${project}/config/settings.cfg"


RUN buildDeps='gcc g++ git-all' && \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends && \
    apt-get install -y httpie && \
    pip install -r /tmp/${project}/requirements.txt && \
    pip install --no-cache-dir /tmp/${project} && \
    rm -r /tmp/${project} && \
    apt-get purge -y --auto-remove $buildDeps

WORKDIR /${project}

COPY ./static /static

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /${project}/config
COPY ./start.py /${project}/start.py

ENV FLASK_APP="pyweb.app:create_app()"
EXPOSE 8000

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir httpretty pytest pytest-cov pytest-html pytest-mock mongomock requests-mock

ENV APPLICATION_SETTINGS="/${project}/test/config/settings.cfg"

