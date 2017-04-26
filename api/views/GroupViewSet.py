from rest_framework import viewsets
from django.contrib.auth.models import Group
from api.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    class Meta:
        app_label = 'api'
