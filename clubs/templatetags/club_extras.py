from django import template
from ..models import Club

register = template.Library()

@register.filter(name='has_club')
def has_club(user, slug):
    club = Club.objects.get(slug=slug)
    return club in user.profile.clubs.all()
