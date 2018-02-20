from django.urls import path, re_path
from .views import *

app_name = 'clubs'
urlpatterns = [
    path('', HomeView.as_view(), name='clubs_home'),
    path('join/<int:pk>', JoinView.as_view(), name='join'),
    path('<int:pk>/qr', QrView.as_view(), name='qr'),
]