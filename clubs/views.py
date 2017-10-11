from django.shortcuts import render, get_object_or_404

# Create your views here.
from clubs.models import Club


def index(request):
    # get all clubs
    clubs = Club.objects
    return render(request, '_home.html', {'clubs': clubs})


def club(request, slug):
    # get the club object
    club = get_object_or_404(Club, slug=slug)
    # now return the rendered template
    return render(request, 'clubs/club.html', {'club': club})