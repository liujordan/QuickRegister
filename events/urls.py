from django.conf.urls import url

from .views import *

app_name = 'events'
urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/join/$', JoinView.as_view(), name='join'),
    url(r'^$', index),
    url(r'^(?P<slug>[\w\-]+)/$', event, name='event'),
]