from django.urls import path, re_path
from .views import *

app_name = 'clubs'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ClubView.as_view(), name='home'),
    path('<int:pk>/join/', JoinView.as_view(), name='join'),
    path('<int:pk>/leave/', LeaveView.as_view(), name='leave'),
    path('<int:pk>/qr', QrView.as_view(), name='qr'),
    path('<int:pk>/members', MembersView.as_view(), name='members'),
    path('<int:pk>/members/export_csv', export_csv, name='export_csv'),
]
