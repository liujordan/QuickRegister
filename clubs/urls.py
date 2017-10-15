from django.conf.urls import url
from django.contrib import admin
from .views import JoinView

from .views import *

app_name = 'clubs'
urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/join/$', JoinView.as_view(), name='join'),
    url(r'^$', index),
    url(r'^(?P<slug>[\w\-]+)/$', club, name='club'),
]