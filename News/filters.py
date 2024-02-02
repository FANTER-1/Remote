import django_filters
from django import template
from django.utils.safestring import mark_safe
from .models import News

register = template.Library()

@register.filter(name='censor')
def censor(value):
    unwanted_words = ['нежелательное_слово1', 'нежелательное_слово2', ...]
    censored_value = value

    for word in unwanted_words:
        censored_value = censored_value.replace(word, '*' * len(word))

    return mark_safe(censored_value)


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    date_added = django_filters.DateFilter(widget=django_filters.widgets.DateInput())

    class Meta:
        model = News
        fields = ['title', 'author', 'date_added']