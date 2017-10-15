from django.conf.urls import url

from .views import *

app_name = 'profiles'
urlpatterns = [
    url(r'^$', view),
    url(r'edit', edit),
    url(r'update', update)
]