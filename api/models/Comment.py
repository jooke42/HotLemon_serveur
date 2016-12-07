from django.db import models
from django.contrib.auth.models import User
from api.models.Topic import Topic


class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    topic = models.ForeignKey(Topic,null=False, default=Topic(), blank=True)
    parent_comment = models.ForeignKey('self', null=True)
    @classmethod
    def create(cls, _author, _body):
        comment = cls(author=_author, body=_body)
        return comment

    class Meta:
        app_label = 'api'
