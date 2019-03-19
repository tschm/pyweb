# Set the base image to beakerx
FROM lobnek/jupyter:v2.5

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@lobnek.com"

USER root

COPY . /tmp/lobnek
RUN pip install --no-cache-dir /tmp/lobnek && rm -r /tmp/lobnek

USER $NB_USER
