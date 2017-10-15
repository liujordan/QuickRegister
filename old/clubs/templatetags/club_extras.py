from django import template

from clubs.models import Club
from events.models import Event

register = template.Library()

@register.filter(name='has_club')
def has_club(user, slug):
    club = Club.objects.get(slug=slug)
    return club in user.profile.clubs.all()

@register.filter(name='has_event')
def has_event(user, slug):
    event = Event.objects.get(slug=slug)
    return event in user.profile.events.all()