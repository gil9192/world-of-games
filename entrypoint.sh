#!/bin/bash

# This filee shoud serve for testing the code,
# not for production deployment 

python manage.py migrate
python manage.py runserver 0.0.0.0:8777
