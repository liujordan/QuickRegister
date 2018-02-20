from django.urls import path, re_path
from .views import *

app_name = 'clubs'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ClubView.as_view(), name='home'),
    path('<int:pk>/join/', JoinView.as_view(), name='join'),
    path('<int:pk>/leave/', LeaveView.as_view(), name='leave'),
]