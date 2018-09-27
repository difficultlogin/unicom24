#!/bin/bash

# Migrations
echo "Migrations"
python manage.py migrate
python manage.py loaddata --format json api/fixtures/data.json

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000