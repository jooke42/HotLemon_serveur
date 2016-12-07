from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)

    @classmethod
    def create(cls, _title):
        component = cls(title=_title)
        return component

    class Meta:
        app_label = 'api'
