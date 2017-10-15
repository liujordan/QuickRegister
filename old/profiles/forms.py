from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms


class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'primary_language',
            'secondary_language',
            # ButtonHolder(
            #     Submit('profile', 'Update Profile', css_class='btn-primary')
            # )
        )
