from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views import View
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
import datetime
from django.urls import reverse


class HomeView(TemplateView):
    template_name = 'clubs/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['clubs'] = Club.objects.all()
        return context


class ClubView(TemplateView):
    template_name = 'clubs/club.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['club'] = get_object_or_404(Club, pk=kwargs['pk'])
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
            return HttpResponse("Successfully joined {}".format(club))
        return HttpResponse("You are already part of {}".format(club))


class QrView(TemplateView):
    template_name = 'clubs/qr.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = get_object_or_404(Club, pk=kwargs['pk'])
        return context

class LeaveView(View):
    def get(self, request, *args, **kwargs):
        club = get_object_or_404(Club, pk=kwargs['pk'])
        membership = Membership.objects.filter(user=self.request.user, club=club)
        if membership:
            membership.delete()
        return HttpResponseRedirect(reverse('clubs:home'))
