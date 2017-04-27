from django.db import models
from django.contrib.auth.models import User
from api.models.Topic import Topic


class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField(max_length=140)
    topic = models.ForeignKey(Topic, null=False)
    parent_comment = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        app_label = 'api'
