from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, UpdateView

from profiles.models import Profile


class ViewProfileView(DetailView):
    model = Profile
    template_name_suffix = "_view"


class ProfileEditView(UpdateView):
    model = Profile
    # fields available for editing
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']
    template_name_suffix = "_edit"
