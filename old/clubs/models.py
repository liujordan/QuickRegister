
from django.core.urlresolvers import reverse
from django.db import models


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

    def get_members(self):
        return self.profile_set.all()

    def get_events(self):
        return self.event_set.all()

