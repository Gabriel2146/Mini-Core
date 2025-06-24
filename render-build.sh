#!/bin/sh
python manage.py migrate --noinput
python manage.py cargar_ejemplo
python manage.py collectstatic --noinput
