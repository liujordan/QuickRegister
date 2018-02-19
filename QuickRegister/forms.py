from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    # year of admission and graduation
    year_of_admission = forms.DateField(help_text="Year of Admission")
    year_of_graduation = forms.DateField(help_text="Expected Year of Graduation")

    # major of studies
    major_of_studies = forms.CharField(help_text="Program of studies")

    # languages
    primary_language = forms.CharField(help_text="Primary Language")
    secondary_language = forms.CharField(help_text="Secondary Language")

    # resume
    resume = forms.FileField(help_text="Resume (Optional)")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'year_of_admission', 'year_of_graduation',
                  'major_of_studies', 'primary_language',
                  'secondary_language', 'resume',)
