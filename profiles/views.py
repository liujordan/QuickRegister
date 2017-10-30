# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/create.html'
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']

    def render_to_response(self, context):
        # if user has already created a profile
        if self.request.user.profile:
            # return HttpResponseRedirect(reverse_lazy('profiles:view-profile', args=[self.request.user.id]))
            return HttpResponse('You already have a profile tho!')
        return super(ProfileCreateView, self).render_to_response(context)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return HttpResponseRedirect(reverse_lazy('profiles:view-profile', args=[self.request.user.id]))

class ProfileHomeView(DetailView):
    model = Profile
    template_name_suffix = "_view"
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']

    def get_object(self, queryset=None):
        return self.request.user.profile

    def render_to_response(self, context, **response_kwargs):
        # create a profile if user dont have one
        if not self.request.user.profile:
            return HttpResponseRedirect(reverse_lazy('create-profile'))
        return super(ProfileHomeView, self).render_to_response(context)

class ProfileEditView(UpdateView):
    model = Profile
    # fields available for editing
    template_name_suffix = "_edit"
    fields = ['primary_language', 'secondary_language', 'major_of_studies',
              'year_of_admission', 'year_of_graduation', 'resume']

    def render_to_response(self, context, **response_kwargs):
        # create a profile if user dont have one
        if not self.request.user.profile:
            return HttpResponseRedirect(reverse_lazy('create-profile'))
        return super(ProfileEditView, self).render_to_response(context)

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('profiles:view-profile', args=[self.request.user.id]))
