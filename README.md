# employee-managment
Install all package
====================
pip install > requirement.txt

Migrate database
=================
python manage.py migrate

Start Run local server
======================
python manage.py runserver

INSTALL DOCKER AND REDIS SERVER
================================
Run redis server into docker contaner
OR
install redis server direct on 6379 port

setup clery settings.py
====================
CELERY_BROKER_URL ="redis://localhost:6379"  # CHANGE THIS URL
CELERY_RESULT_BACKEND ="redis://localhost:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER ='json'

RUN CELEY WORKER ON TERMINAL
============================
celery -A worker mb -l info


