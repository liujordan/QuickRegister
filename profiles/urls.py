from django.conf.urls import url

from .views import *

app_name = 'profiles'
urlpatterns = [
    url(r'^$', ViewProfileView.as_view(), name="view-profile"),
]
