from django.shortcuts import render, get_object_or_404

# Create your views here.
from clubs.models import Club
from profiles.models import Membership
import logging

logger = logging.getLogger(__name__)
def index(request):
    # get all clubs
    clubs = Club.objects
    return render(request, 'clubs/_home.html', {'clubs': clubs})


def club(request, slug):
    # get the club object
    club = get_object_or_404(Club, slug=slug)
    # now return the rendered template
    return render(request, 'clubs/club.html', {'club': club})

def join(request, slug):
    logger.info("Triggered")
    # get the club to join
    club = get_object_or_404(Club, slug=slug)
    user = request.user

    if not user.is_authenticated():
        logger.info("User not auth")
        return

    # check if user is part of club
    if club.profile_set.filter(username=user.username).exists():
        logger.info("User already part of club")
        return

    Membership.objects.create(
        profile=user.profile,
        club=club
    )
    return render(request, 'clubs/clubs.html', {'club': club})
    # add this user to the intermediate table

