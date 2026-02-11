#!/bin/bash

exec celery --app tasks.celery worker --beat --loglevel=info
