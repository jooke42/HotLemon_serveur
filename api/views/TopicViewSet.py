from rest_framework import viewsets
from api.models import Topic
from api.serializers import TopicSerializer
from rest_framework.pagination import CursorPagination


class CustomCursor(CursorPagination):
    ordering = 'vote_for'


class TopicViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    class Meta:
        app_label = 'api'
        model = Topic
