from django.db import models

from apps.clubs.models import Club


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    clubs = models.ManyToManyField('clubs.Club', blank=True)

    def __str__(self):
        return self.email