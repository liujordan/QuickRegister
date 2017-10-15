from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Profile(models.Model):
    """ Model for a profile of a user, storing additional details of a user """

    # slug for profile
    slug = models.SlugField(max_length=255, blank=True)

    # user display name
    display_name = models.CharField(max_length=100)

    # one to one relationship with a user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # year of admission and graduation
    year_of_admission = models.DateField(blank=True)
    year_of_graduation = models.DateField(blank=True)

    # major of studies
    major_of_studies = models.CharField(max_length=50, blank=True)

    # languages
    primary_language = models.CharField(max_length=30, blank=True)
    secondary_language = models.CharField(max_length=30, blank=True)

    # resume
    resume = models.FileField(upload_to='uploads/resume', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.display_name)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        """ (Profile) -> str
        Returns the full name of a user
        """
        return self.user.first_name + " " + self.user.last_name
