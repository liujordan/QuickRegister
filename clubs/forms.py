from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile
from .models import Club

class ClubForm(forms.ModelForm):
  class Meta:
    model = Club
    fields = ('name', 'description')

# class SignUpForm(UserCreationForm):

#     # year of admission and graduation
#     year_of_admission = forms.DateField(help_text="Year of Admission (YYYY-MM-DD)")
#     year_of_graduation = forms.DateField(help_text="Expected Year of Graduation (YYYY-MM-DD)")

#     # major of studies
#     major_of_studies = forms.CharField(help_text="Program of studies")

#     # languages
#     primary_language = forms.CharField(help_text="Primary Language")
#     secondary_language = forms.CharField(help_text="Secondary Language")

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2',
#                   'year_of_admission', 'year_of_graduation',
#                   'major_of_studies', 'primary_language',
#                   'secondary_language',)


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('year_of_admission', 'year_of_graduation',
#                   'major_of_studies', 'primary_language',
#                   'secondary_language',)
