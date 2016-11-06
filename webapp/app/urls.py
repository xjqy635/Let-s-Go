from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'test/$', views.test),
    url(r'user/login/$', views.user_login),
    url(r'user/logout/$', views.user_logout),
    url(r'user/register/$', views.user_register),
]
