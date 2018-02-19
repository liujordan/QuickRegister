from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views import View
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import datetime
from django.http import HttpResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'clubs/join.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['clubs'] = Club.objects.all()
        return context

class JoinView(View):
    def get(self, request, *args, **kwargs):
        club = get_object_or_404(Club, pk=kwargs['pk'])
        if not Membership.objects.filter(user=self.request.user, club=club):
            membership = Membership(
                user=self.request.user,
                club=club,
                date_joined=datetime.datetime.now())
            membership.save()
            return HttpResponse("kill me cuz i joined a club")
        return HttpResponse("kill me cuz im lonely")
