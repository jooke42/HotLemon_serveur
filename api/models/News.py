from django.db import models
from api.models.Topic import Topic


class News(Topic):
    picture = models.ImageField(upload_to='pictures', max_length=254)

    class Meta:
        app_label = 'api'
