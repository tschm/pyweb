FROM python:3.8.7-buster as builder

# COPY this project into a local folder and install from there
COPY . /tmp/server

#RUN apt-get update && \
#    apt-get install -y \
#            #"g++=4:6.3.0-4" \
#            "git=1:2.11.0-3+deb9u7" \
#            "httpie=0.9.8-1" \
#            --no-install-recommends && \
RUN pip install -r /tmp/server/requirements.txt && \
    rm -r /tmp/server
    #&& \
#    apt-get purge -y --auto-remove "g++" "git" && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

WORKDIR /server

COPY ./static /static
COPY ./pyweb  /server/pyweb

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as web

# Install the webpage
COPY ./config /server/config
COPY ./start.py /server/start.py

ENV APPLICATION_SETTINGS="/server/config/settings.cfg"
#ENV FLASK_APP="pyweb.app:create_app()"
EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["/server/start.py"]

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

COPY ./test /server/test

ENV APPLICATION_SETTINGS="/server/test/config/settings.cfg"

RUN pip install --no-cache-dir -r /server/test/requirements.txt


