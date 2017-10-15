from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from quickregister.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create a user profile if it is not already created """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    """ Save a user profile to the database """
    instance.profile.save()