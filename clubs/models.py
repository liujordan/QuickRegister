from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import EmailField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Club(models.Model):
    """ A model for a club """
    club_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.club_name

    def get_absolute_url(self):
        return reverse('clubs.views.club', args=[self.slug])


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


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()