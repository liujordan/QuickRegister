
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

    def get_first_member(self):
        return ", ".join([str(x.user.username) for x in self.profile_set.all()])

