#!/bin/sh

source venv/bin/activate
flask db init
flask db upgrade
exec gunicorn -b :8081 --access-logfile - --error-logfile - backend:app
