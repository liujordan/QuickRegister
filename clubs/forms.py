from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'primary_language',
            'secondary_language',
            ButtonHolder(
                Submit('profile', 'Update Profile', css_class='btn-primary')
            )
        )

    class Meta:
        model = User.profile
        fields = ("primary_language", "secondary_language")
