release: python thegamehistorico/manage.py migrate
web: gunicorn --pythonpath thegamehistorico thegamehistorico.wsgi --log-file - 