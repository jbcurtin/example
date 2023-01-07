#!/usr/bin/env bash

if [ "$MIGRATE_DB" == "yes" ]; then
    sleep 10
    ./manage.py migrate
fi
gunicorn -b 0.0.0.0:8000 -w 4 sustainability_page.wsgi:application
