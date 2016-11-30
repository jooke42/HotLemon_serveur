from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)

    @classmethod
    def create(cls, title):
        component = cls(title=title)
        # do something with the book
        return component

    class Meta:
        abstract = True
