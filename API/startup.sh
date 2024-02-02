#!/bin/bash
python3 -m pip install virtualenv
python3 -m virtualenv virtual
source virtual/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
