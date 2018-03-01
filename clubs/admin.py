from django.contrib import admin
from .models import *
from django.http import HttpResponse

admin.site.register(Membership)
admin.site.register(Club)