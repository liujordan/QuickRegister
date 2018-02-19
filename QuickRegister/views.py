from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
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
def home(request):
    return render(request, 'home.html')