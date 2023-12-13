release: python manage.py migrate
web: gunicorn rileyimmeldotcom.wsgi
worker: python -u run-worker.py
