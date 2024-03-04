from celery import shared_task
import time

from celery import Celery
from celery.decorators import task
from django.core.mail import send_mail


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@task
def send_notification(email, message):
    send_mail('Notification', message, 'from@example.com', [email])