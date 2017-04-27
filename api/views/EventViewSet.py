from rest_framework import viewsets
from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    class Meta:
        app_label = 'api'
        model = Event
