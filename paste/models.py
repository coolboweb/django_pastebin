from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


VISIBILITY_CHOICES = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
)


class Paste(models.Model):
    title = models.CharField(max_length=70, default='Untitled')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    visibility = models.CharField(max_length=8, choices=VISIBILITY_CHOICES, default='PUBLIC')
    expire_date = models.DateTimeField(null=True, blank=True, default=None)
    author = models.ForeignKey(User, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.title
