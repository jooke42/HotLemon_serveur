from django.db import models
from api.models.Topic import Topic


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    topics = models.ManyToManyField(Topic, null=False, blank=True)
    parent_comment = models.ForeignKey('self', blank=True, null=True)

    def get_username(self):
        return self.username

    class Meta:
        app_label = 'api'
