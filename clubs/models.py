from django.db import models
from django.core.urlresolvers import reverse


class Club(models.Model):
    """ A model for a club """
    club_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.club_name)

    def get_absolute_url(self):
        return reverse('clubs.views.club', args=[self.slug])
