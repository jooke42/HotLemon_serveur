from rest_framework import viewsets
from api.models import Topic
from api.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Topic.Topic.objects.all()
    serializer_class = TopicSerializer

    class Meta:
        app_label = 'api'
