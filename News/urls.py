from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
