# Set the base image to Ubuntu
FROM lobnek/docker:v1.3 as builder

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY ./pyweb /pyweb/pyweb
COPY ./config /pyweb/config

COPY ./start.py /pyweb/start.py
#COPY ./caching.py /pyrisk/caching.py
#COPY ./build_whoosh.py /pyrisk/build_whoosh.py

WORKDIR pyweb

ENV APPLICATION_SETTINGS="/pyweb/config/server_settings.cfg"

EXPOSE 8000

# ----------------------------------------------------------------------------------------------------------------------
FROM builder as test

RUN pip install --no-cache-dir httpretty pytest pytest-cov pytest-html pytest-mock attrdict
COPY ./test            /pyweb/test

ENV APPLICATION_SETTINGS="/pyweb/test/server_settings.cfg"

CMD py.test --cov=pyweb --cov-report html:artifacts/html-coverage --cov-report term --html=artifacts/html-report/report.html test