from __future__ import absolute_import

from braces.views import MessageMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse

from clubs.models import Club
from profiles.models import Membership

import logging

logger = logging.getLogger(__name__)
class JoinView(MessageMixin, generic.RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        slug = kwargs['slug']
        if not user.is_authenticated:
            return HttpResponse("You need to log in boi!")
        if user.profile.clubs.filter(slug=slug).exists():
            return HttpResponse("Already part of this club tho!")
        join_club(request, slug)
        self.url = reverse('clubs:club', args={slug})
        self.messages.success("You've joined the club!")
        return super(JoinView, self).get(request, *args, **kwargs)

def index(request):
    # get all clubs
    clubs = Club.objects
    return render(request, 'clubs/_home.html', {'clubs': clubs})


def club(request, slug):
    # get the club object
    club = get_object_or_404(Club, slug=slug)
    # now return the rendered template
    return render(request, 'clubs/club.html', {'club': club})

def join_club(request, slug):
    logger.info("Triggered")
    # get the club to join
    club = get_object_or_404(Club, slug=slug)
    user = request.user

    if not user.is_authenticated():
        logger.info("User not auth")
        return

    # check if user is part of club
    if club.profile_set.filter(id=user.id).exists():
        logger.info("User already part of club")
        return

    Membership.objects.create(
        profile=user.profile,
        club=club
    )
    return render(request, 'clubs/club.html', {'club': club})
    # add this user to the intermediate table

