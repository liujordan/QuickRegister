from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """ Model for a profile of a user, storing additional details of a user """

    # one to one relationship with a user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # year of admission and graduation
    year_of_admission = models.DateField(null=True)
    year_of_graduation = models.DateField(null=True)

    # major of studies
    major_of_studies = models.CharField(max_length=50, null=True)

    # languages
    primary_language = models.CharField(max_length=30, null=True)
    secondary_language = models.CharField(max_length=30, null=True)

    # resume
    resume = models.FileField(upload_to='uploads/resume', null=True)

    def __str__(self):
        """ (Profile) -> str
        Returns the full name of a user
        """
        return self.user.username + "'s Profile"

    def get_absolute_url(self):
        return u'/profile/{}'.format(self.id)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()