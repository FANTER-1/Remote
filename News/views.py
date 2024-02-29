from django.shortcuts import render
from django_filters.views import FilterView
from .filters import NewsFilter

from .models import News
from django.template.defaulttags import register
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

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












