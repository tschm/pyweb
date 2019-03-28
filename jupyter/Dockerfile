# Set the base image to beakerx
FROM lobnek/jupyter:v2.8

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

# COPY this project into a local folder and install from there
COPY --chown=beakerx:beakerx . /tmp/lobnek

RUN pip install --no-cache-dir /tmp/lobnek && \
    rm -r /tmp/lobnek
