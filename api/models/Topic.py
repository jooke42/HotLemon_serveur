from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    body = models.TextField(max_length=500)
    published_date = models.DateTimeField
    finished_date = models.DateTimeField

    class Meta:
        app_label = 'api'
