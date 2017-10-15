from __future__ import absolute_import

import logging

from braces.views import MessageMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from events.models import Event
from profiles.models import Attendee

logger = logging.getLogger(__name__)
class JoinView(MessageMixin, generic.RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        slug = kwargs['slug']
        if not user.is_authenticated:
            return HttpResponse("You need to log in boi!")
        if user.profile.events.filter(slug=slug).exists():
            return HttpResponse("Already part of this event tho!")
        join_event(request, slug)
        self.url = reverse('events:event', args={slug})
        self.messages.success("You've joined the event!")
        return super(JoinView, self).get(request, *args, **kwargs)

def index(request):
    # get all clubs
    events = Event.objects
    return render(request, 'clubs/_home.html', {'events': events})


def event(request, slug):
    # get the club object
    events = get_object_or_404(Event, slug=slug)
    # now return the rendered template
    return render(request, 'events/event.html', {'events': events})

def join_event(request, slug):
    # get the club to join
    event = get_object_or_404(Event, slug=slug)
    user = request.user

    if not user.is_authenticated():
        logger.info("User not auth")
        return

    # check if user is part of club
    if event in user.profile.events.all():
        logger.info("User already part of club")
        return

    Attendee.objects.create(
        profile=user.profile,
        event=event
    )
    return render(request, 'events/event.html', {'events': event})
    # add this user to the intermediate table

