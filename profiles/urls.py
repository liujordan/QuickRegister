from django.conf.urls import url

from .views import *

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ViewProfileView.as_view(), name="view-profile"),
    url(r'^(?P<pk>\d+)/edit/', ProfileEditView.as_view(), name="edit-profile")
]
