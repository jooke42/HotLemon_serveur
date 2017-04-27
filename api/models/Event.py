from django.db import models
from api.models.Address import Address
from api.models.Topic import Topic


class Event(Topic):
    place = models.ForeignKey(Address, null=False, blank=True)

    class Meta:
        app_label = 'api'
