from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User)
    body = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='pictures', max_length=254, blank=True)
    published_date = models.DateTimeField
    finished_date = models.DateTimeField
    created = models.DateTimeField(auto_now_add=True)
    vote_for = models.IntegerField(default=0)
    vote_against = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    streetNumber = models.CharField(max_length=5)
    street = models.CharField(max_length=60)
    postalCode = models.CharField(max_length=5)

    class Meta:
        app_label = 'api'
