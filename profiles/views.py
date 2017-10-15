from profile import Profile

from braces.views import MessageMixin
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy


def update(request):
    """ Updates the user's profile """
    if request.user.is_authenticated():
        request.user.profile.primary_language = request.POST['primary_language']
        request.user.profile.secondary_language = request.POST['secondary_language']
        request.user.save()

    return render(request, 'profiles/edit_profile.html', {'user': request.user})


def edit(request):
    """ Returns the edit view of the user """
    user = _redirect_if_not_logged_in(request)

    # return the view profile template
    return render(request, 'profiles/edit_profile.html', {'user': user})


def view(request):
    """ Returns the profile of the current user"""
    user = _redirect_if_not_logged_in(request)

    # return the view profile template
    return render(request, 'profiles/view_profile.html', {'user': user})


def _redirect_if_not_logged_in(request):
    # return the user object if available
    if request.user.is_authenticated():
        return request.user
    else:
        # redirect non user to homepage
        return redirect(reverse_lazy('home'))

