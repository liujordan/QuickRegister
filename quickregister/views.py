from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def redirect_if_logged_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        return login(request)
