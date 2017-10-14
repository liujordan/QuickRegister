from django.contrib import admin

# Register your models here.
from clubs.models import Club
from profiles.models import Profile, Membership

admin.site.register(Club)
admin.site.register(Profile)
admin.site.register(Membership)