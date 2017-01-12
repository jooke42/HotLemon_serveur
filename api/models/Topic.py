from django.db import models
from django.contrib.auth.models import User
from api.models.Component import Component


class Topic(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    components = models.ManyToManyField(Component, blank=True)
    published_date = models.DateTimeField
    finished_date = models.DateTimeField

    class Meta:
        app_label = 'api'
