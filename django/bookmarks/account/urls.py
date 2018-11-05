from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.dashbord, name='dashbord'),
]
