# from django import template
# from ..models import Event
#
# register = template.Library()
#
# @register.filter(name='has_event')
# def has_event(user, slug):
#     event = Event.objects.get(slug=slug)
#     return event in user.profile.events.all()
