from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)

    @classmethod
    def create(cls, _title, _user):
        component = cls(title=_title, author=_user)
        return component

    class Meta:
        app_label = 'api'
