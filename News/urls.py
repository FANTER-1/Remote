from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    ...
]
