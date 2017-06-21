from rest_framework import viewsets
from django.contrib.auth.models import Group
from api.serializers import GroupSerializer
from rest_framework.pagination import CursorPagination


class CustomCursor(CursorPagination):
    ordering = 'id'


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomCursor

    class Meta:
        app_label = 'api'
        model = Group
