from django.core.urlresolvers import reverse
from django.db import models

from clubs.models import Club


# Create your models here.
class Event(models.Model):
    """ Model for an event"""
    event_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_end = models.DateField(blank=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('clubs.views.club', args=[self.slug])

    def get_members(self):
        return ", ".join([str(x) for x in self.profile_set.all()])