"""QuickRegister URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
import clubs.urls

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', auth_views.login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('profile/', update_profile, name="edit_profile"),
    path('admin/', admin.site.urls),
    path('clubs/', include('clubs.urls')),
]
