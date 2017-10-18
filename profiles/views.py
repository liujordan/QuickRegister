# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView

from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/create.html'
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']

class ProfileHomeView(DetailView):
    model = Profile
    template_name_suffix = "_view"
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']

class ProfileEditView(UpdateView):
    model = Profile
    # fields available for editing
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']
    template_name_suffix = "_edit"
