release: python TheGameHistorico/manage.py migrate
web: gunicorn --pythonpath TheGameHistorico TheGameHistorico.wsgi --log-file - 