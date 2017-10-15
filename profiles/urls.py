from django.conf.urls import url

from .views import *

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', ViewProfileView.as_view(), name="view-profile"),
    url(r'^(?P<slug>[-\w]+)/edit/', ProfileEditView.as_view(), name="edit-profile")
]
