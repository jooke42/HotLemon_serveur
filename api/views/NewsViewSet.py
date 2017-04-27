from rest_framework import viewsets
from api.models import News
from api.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    class Meta:
        app_label = 'api'
        model = News
