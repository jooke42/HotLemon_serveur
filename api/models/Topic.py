from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    published_date = models.DateTimeField
    finished_date = models.DateTimeField

    def get_username(self):
        return self.username

    class Meta:
        app_label = 'api'
