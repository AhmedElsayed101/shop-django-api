#!/bin/bash

while getopts v:a:p: flag
do
    case "${flag}" in
        v) PYTHON_VERSION=${OPTARG};;
        a) APP_VERSION=${OPTARG};;
        p) BROADCAST_PORT_BACKEND=${OPTARG};;
    esac
done


cat > ./dev.env <<EOD
COMPOSE_PROJECT_NAME=shop-dev

DEBUG=1


SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres_dev
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432


SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]


PYTHON_VERSION=$PYTHON_VERSION

APP_VERSION=$APP_VERSION

BROADCAST_PORT_BACKEND=$BROADCAST_PORT_BACKEND
EOD
