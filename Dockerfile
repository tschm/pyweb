FROM python:3.7.7-slim-stretch as builder

# COPY this project into a local folder and install from there
COPY . /tmp/server

#RUN buildDeps='g++ git' && \
#    apt-get update && apt-get install -y $buildDeps --no-install-recommends && \
RUN apt-get update && \
    apt-get install -y \
            "g++" \
            "git" \
            "httpie=0.9.8-1" \
            --no-install-recommends && \
    pip install -r /tmp/server/requirements.txt && \
    pip install --no-cache-dir /tmp/server && \
    rm -r /tmp/server && \
    apt-get purge -y --auto-remove "g++" "git" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /server

COPY ./static /static

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /server/config
COPY ./start.py /server/start.py

ENV APPLICATION_SETTINGS="/server/config/settings.cfg"
ENV FLASK_APP="pyweb.app:create_app()"
EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["/server/start.py"]

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir pytest pytest-cov pytest-html pytest-mock mongomock requests-mock

ENV APPLICATION_SETTINGS="/server/test/config/settings.cfg"

