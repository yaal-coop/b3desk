FROM python:3.11-bullseye

# Install.
RUN \
  apt update && \
  apt -y upgrade && \
  apt install -y gcc libpq-dev

RUN pip install --upgrade pip setuptools wheel

COPY requirements.app.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY misc/wsgi.py misc/gunicorn.py misc/run_webserver.sh /opt/bbb-visio/
COPY misc/job.cron /etc/cron.d/job
RUN chmod u+x /opt/bbb-visio/run_webserver.sh
COPY migrations /opt/bbb-visio/migrations
COPY b3desk /opt/bbb-visio/b3desk

WORKDIR /opt/bbb-visio/
ENTRYPOINT ["/opt/bbb-visio/run_webserver.sh"]
