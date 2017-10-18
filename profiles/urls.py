from django.conf.urls import url

from .views import *

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileHomeView.as_view(), name="view-profile"),
    url(r'^(?P<pk>\d+)/create/$', ProfileCreateView.as_view(), name="create-profile"),
    url(r'^(?P<pk>\d+)/edit/$', ProfileEditView.as_view(), name="edit-profile"),
]
