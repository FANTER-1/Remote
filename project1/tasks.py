from celery import shared_task
import time

from celery import Celery
from celery.decorators import task
from django.core.mail import send_mail

app = Celery('tasks', broker='redis://localhost:6379/0')

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@task
def send_notification(email, message):
    send_mail('Notification', message, 'nazarenko.vitaliy111cool2016@mail.ru', [email])

@app.task
def send_notification(article_id=None):
    # Логика отправки уведомлений подписчикам категории статьи
    pass
