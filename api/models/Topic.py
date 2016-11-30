from django.db import models
from django.contrib.auth.models import User
from .Component import Component


class Topic(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    components = models.ManyToManyField(Component)

    @classmethod
    def create(cls):
        topic = cls()
        # do something with the book
        return topic
