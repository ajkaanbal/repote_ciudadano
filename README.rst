INSTALL
=======

Please, create a virtalenv

1. pip install -r requeriments/dev.txt
2. export SECRET_KEY='Your secret key'
3. export DJANGO_SETTINGS_MODULE=reporte_ciudadano.settings.dev
4. cd reporte_ciudadano
5. ./manage.py syncdb
6. ./manage.py migrate
7. ./manage.py runserver

Done!
