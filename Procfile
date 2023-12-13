release: python manage.py migrate
web: gunicorn mainsite.wsgi --log-file -
worker: python -u run-worker.py