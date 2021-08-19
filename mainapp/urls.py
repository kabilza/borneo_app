from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('index', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
]