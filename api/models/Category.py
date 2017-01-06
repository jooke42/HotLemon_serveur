from django.db import models
from api.models.Topic import Topic

#TODO implement class
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    topics = models.ManyToManyField(Topic, null=False, blank=True)
    parent_comment = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        app_label = 'api'
