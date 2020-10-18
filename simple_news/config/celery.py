from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# https://docs.celeryproject.org/en/stable/index.html

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_transport_options = {'visibility_timeout': 3600}

app.autodiscover_tasks()
