from django.conf.urls import url
from django.contrib import admin

from .views import *
app_name = 'clubs'
urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<slug>[\w\-]+)/$', club),
    url(r'^(?P<slug>[\w\-]+)/join/$', join)
]