release: python manage.py migrate
web: gunicorn rileyimmeldotcom.wsgi --log-file -
worker: python -u run-worker.py