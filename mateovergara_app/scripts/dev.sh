#!/bin/sh

# evita error de permisos
chown -R mateovergara_app:mateovergara_app /app
chown -R mateovergara_app:mateovergara_app /home/app

exec su -m mateovergara_app -c 'python manage.py runserver 0.0.0.0:8000'
