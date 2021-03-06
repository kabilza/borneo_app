from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup_view, name='signup'),
    path('index', views.index, name='index'),
    path('index/profile', views.profile_view, name='profile'),
    path('index/tutorial', views.tutorial, name='tutorial'),
    path('index/battery-list', views.battery_list, name='battery-list'),
    path('index/battery-remove/<int:id>', views.battery_remove, name='battery-remove'),
    path('index/profile-edit', views.profile_edit, name='profile-edit'),
    path('index/name-edit', views.username_edit, name='username-edit'),
    path('register-battery', views.battery_registration, name='register-battery'),
    path('', views.welcome, name='welcome'),
    path('index/warranty', views.warranty_con, name='warranty_con'),
    path('social-auth/', include('social_django.urls', namespace="social"))
]