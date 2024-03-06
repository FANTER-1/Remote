import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

app = Celery('project1')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app = Celery('myapp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(7*24*3600, send_notification.s('nazarenko.vitaliy111cool2016@mail.ru', 'Weekly notification'), name='send-notification')
