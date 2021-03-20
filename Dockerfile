FROM python:3.8.7-buster as builder

# COPY this project into a local folder and install from there
COPY . /tmp/server

RUN pip install -r /tmp/server/requirements.txt && \
    rm -r /tmp/server

WORKDIR /server

COPY ./static /static
COPY ./pyweb  /server/pyweb

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /server/config
COPY ./start.py /server/start.py

ENV APPLICATION_SETTINGS="/server/config/settings.cfg"
EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["/server/start.py"]

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

COPY ./test /server/test

ENV APPLICATION_SETTINGS="/server/test/config/settings.cfg"

RUN pip install --no-cache-dir -r /server/test/requirements.txt


