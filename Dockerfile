# Set the base image to beakerx
FROM continuumio/miniconda3 as builder

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# COPY this project into a local folder and install from there
COPY . /tmp/lobnek

ENV APPLICATION_SETTINGS="/pyweb/config/server_settings.cfg"

RUN conda install -c conda-forge nomkl pandas=0.24.2 requests=2.21.0 && \
    conda clean -y --all && \
    pip install -r /tmp/lobnek/requirements.txt && \
    pip install --no-cache-dir /tmp/lobnek && \
    rm -r /tmp/lobnek

WORKDIR /pyweb


# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /pyweb/config
COPY ./start.py /pyweb/start.py
EXPOSE 8000
EXPOSE 8050

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

ENV CHROMEDRIVER_VERSION=77.0.3865.40 \
    CHROMEDRIVER_DIR=/chromedriver \
    PATH=/chromedriver:$PATH

# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get install -y wget xvfb unzip gnupg2 && \
    # Set up the Chrome PPA
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    # Update the package list and install chrome
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    mkdir $CHROMEDRIVER_DIR && \
    wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR && \
    google-chrome --version

RUN pip install --no-cache-dir httpretty pytest pytest-cov pytest-html pytest-mock sqlalchemy_utils selenium dash[testing]

ENV APPLICATION_SETTINGS=/pyweb/test/server_settings.cfg

CMD py.test --cov=pyweb --cov-report html:artifacts/html-coverage --cov-report term --html=artifacts/html-report/report.html /pyweb/test
