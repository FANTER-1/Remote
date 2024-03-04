from django.shortcuts import render,  reverse, redirect
from django_filters.views import FilterView
from .filters import NewsFilter

from .models import News
from django.template.defaulttags import register
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from django.views import View
from django.core.mail import mail_admins
from datetime import datetime

from .models import Appointment
from django.template.loader import render_to_string

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers

@register.filter
def censor(value):
    bad_words = ['нежелательное_слово1', 'нежелательное_слово2']  # список нежелательных слов
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value

def news_list(request):
    news = News.objects.order_by('-publish_date')  # отсортировать новости по дате публикации
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


class PaginationMixin:
    pass


class NewsListView(PaginationMixin, ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    ordering = ['-date_added']

class NewsSearchView(FilterView):
    model = News
    template_name = 'news_search.html'
    filterset_class = NewsFilter

class ProfileEditView(LoginRequiredMixin, UpdateView):
    ...

Group.objects.create(name='common')
Group.objects.create(name='authors')


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        mail_admins(
            subject=f'{appointment.client_name} {appointment.date.strftime("%d %m %Y")}',
            message=appointment.message,
        )

        return redirect('appointments:make_appointment')


def notify_managers_appointment(sender, instance, created, **kwargs):
    subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )








