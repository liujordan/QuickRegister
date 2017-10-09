from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from braces import views
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "_home.html"


class SignUpView(generic.CreateView, views.AnonymousRequiredMixin, views.FormValidMessageMixin):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
    form_valid_message = "Successfully signed up."


class LoginView(generic.FormView, views.AnonymousRequiredMixin, views.FormValidMessageMixin):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'
    form_valid_message = "You are now logged in."

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView, views.LoginRequiredMixin, views.MessageMixin):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)