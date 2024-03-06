from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from background_task import background


class News(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # другие поля, если необходимо

    def __str__(self):
        return self.email

def send_notification(news):
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        subject = 'Новая новость: {}'.format(news.title)
        message = render_to_string('email/notification.html', {'news': news})
        send_mail(subject, message, 'nazarenko.vitaliy111cool2016@mail.ru', [subscriber.email], fail_silently=False)

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    send_notification(self)

@background(schedule=timezone.now())
def weekly_newsletter():
    latest_news = News.objects.order_by('-pub_date')[:5]
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        subject = 'Еженедельная рассылка новостей'
        message = render_to_string('email/weekly_news.html', {'news': latest_news})
        send_mail(subject, message, 'nazarenko.vitaliy111cool2016@mail.ru', [subscriber.email], fail_silently=False)
