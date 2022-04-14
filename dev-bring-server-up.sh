#!/bin/bash


pip install virtualenv
cd app
virtualenv ./env
source ./env/bin/activate
pip install -r requirements.txt
cd shop_project
python manage.py migrate
python manage.py runserver 0.0.0.0:8000