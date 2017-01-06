from django.db import models
from django.contrib.auth.models import User
from api.models.Topic import Topic


class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField(max_length=140)
    topic = models.ForeignKey(Topic, null=False)
    parent_comment = models.ForeignKey('self', blank=True, null=True)

    @classmethod
    def create(cls, _author, _body, _topic):
        comment = cls(author=_author, body=_body, topic=_topic)
        return comment

    class Meta:
        app_label = 'api'
