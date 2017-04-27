from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    streetNumber = models.CharField(max_length=5)
    street = models.CharField(max_length=60)
    postalCode = models.CharField(max_length=5)

    class Meta:
        app_label = 'api'
