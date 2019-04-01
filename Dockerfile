# Set the base image to beakerx
FROM lobnek/jupyter:v2.8 as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# COPY this project into a local folder and install from there
COPY --chown=beakerx:beakerx . /tmp/lobnek
ENV APPLICATION_SETTINGS="/pyweb/config/server_settings.cfg"

RUN pip install --no-cache-dir /tmp/lobnek && \
    pip install -r /tmp/lobnek/requirements.txt && \
    rm -r /tmp/lobnek

# --------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /pyweb/config
COPY ./start.py /pyweb/start.py
EXPOSE 8000
ENV APPLICATION_SETTINGS="/pyweb/config/server_settings.cfg"

WORKDIR /pyweb

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir httpretty pytest==4.3.1 pytest-cov pytest-html pytest-mock

COPY --chown=beakerx:beakerx test ${WORK}/test

ENV APPLICATION_SETTINGS=${WORK}/test/server_settings.cfg

CMD py.test --cov=pyweb --cov-report html:artifacts/html-coverage --cov-report term --html=artifacts/html-report/report.html ${WORK}/test


