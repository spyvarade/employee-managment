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
Run redis server into docker contaner <br />
OR <br />
install redis server direct on 6379 port <br />

setup clery settings.py
====================
CELERY_BROKER_URL ="redis://localhost:6379"  # CHANGE THIS URL <br />
CELERY_RESULT_BACKEND ="redis://localhost:6379" <br />
CELERY_ACCEPT_CONTENT = ['application/json'] <br />
CELERY_RESULT_SERIALIZER = 'json' <br />
CELERY_TASK_SERIALIZER ='json' <br />

RUN CELEY WORKER ON TERMINAL
============================
celery -A worker mb -l info


