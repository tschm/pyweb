FROM python:3.7.7-slim-stretch as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# COPY this project into a local folder and install from there
COPY . /tmp/server

ENV APPLICATION_SETTINGS="/server/config/settings.cfg"

RUN buildDeps='gcc g++ git-all' && \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends && \
    pip install -r /tmp/server/requirements.txt && \
    pip install --no-cache-dir /tmp/server && \
    rm -r /tmp/server && \
    apt-get purge -y --auto-remove $buildDeps

WORKDIR /server


# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /server/config
COPY ./start.py /server/start.py
EXPOSE 8000
EXPOSE 8050

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir httpretty pytest pytest-cov pytest-html pytest-mock mongomock

ENV APPLICATION_SETTINGS=/server/test/config/settings.cfg

COPY test /server/test

CMD py.test --cov=pyweb --cov-report html:artifacts/html-coverage --cov-report term --html=artifacts/html-report/report.html /server/test
