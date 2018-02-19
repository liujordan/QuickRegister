from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # profile fields
            user.profile.year_of_admission = form.cleaned_data.get('year_of_admission')
            user.profile.year_of_graduation = form.cleaned_data.get('year_of_graduation')
            user.profile.major_of_studies = form.cleaned_data.get('major_of_studies')
            user.profile.primary_language = form.cleaned_data.get('primary_language')
            user.profile.secondary_language = form.cleaned_data.get('secondary_language')
            user.profile.resume = form.cleaned_data.get('resume')

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def home(request):
    return render(request, 'home.html')