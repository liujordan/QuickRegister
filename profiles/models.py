from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import EmailField

from clubs.models import Club


class Profile(models.Model):
    """ Model for a profile of a user, storing additional details of a user """
    # one to one relationship with a user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields
    email = EmailField(max_length=254)

    # languages
    primary_language = models.CharField(max_length=30)
    secondary_language = models.CharField(max_length=30)

    # resume
    resume = models.FileField(upload_to='uploads/')

    # clubs for a profile
    clubs = models.ManyToManyField(Club, through='Membership')

    # @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        """ Returns the string representation for a profile """
        return self.user.username


class Membership(models.Model):
    """ Model for the membership. Acts as an intermediary model of Profile and Club"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_requested = models.DateField(auto_now_add=True, blank=True)
    accepted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ["date_requested"]