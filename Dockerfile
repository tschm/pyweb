# Set the base image to beakerx
FROM lobnek/docker:1.9 as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# COPY this project into a local folder and install from there
COPY . /tmp/lobnek

ENV APPLICATION_SETTINGS="/pyweb/config/server_settings.cfg"

RUN pip install -r /tmp/lobnek/requirements.txt && \
    pip install --no-cache-dir /tmp/lobnek && \
    rm -r /tmp/lobnek

WORKDIR /pyweb


# --------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /pyweb/config
COPY ./start.py /pyweb/start.py
EXPOSE 8000
EXPOSE 8050

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir httpretty pytest==4.3.1 pytest-cov pytest-html pytest-mock sphinx sqlalchemy_utils

ENV APPLICATION_SETTINGS=/pyweb/test/server_settings.cfg

CMD py.test --cov=pyweb --cov-report html:artifacts/html-coverage --cov-report term --html=artifacts/html-report/report.html /pyweb/test
