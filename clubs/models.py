from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Club(models.Model):
    """ A model for a club """
    name = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse('clubs.views.club', args=[self.slug])

    def get_first_member(self):
        return ", ".join([str(x.user.username) for x in self.profile_set.all()])

    def get_members(self):
        return self.profile_set.all()

    def get_join_url(self):
        return reverse('clubs:join', args=(self.id,))

    def get_owners(self):
        return Membership.objects.filter(club=self, is_owner=True)

    def get_staff(self):
        return Membership.objects.filter(club=self, is_staff=True)

    def is_member(self, user):
        return Membership.objects.filter(club=self, user=user)

    def add_member(self, user, staff=False, owner=False):
        if self.is_member(user):
            return
        membership = Membership(
            user=user,
            club=self,
            date_joined=datetime.datetime.now(),
            is_staff=staff,
            is_owner=owner)
        membership.save()
        return membership



    # def get_events(self):
        # return self.event_set.all()


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
