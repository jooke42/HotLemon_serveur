from rest_framework import viewsets
from api.models import Address
from api.serializers import CommentSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Address.objects.all()
    serializer_class = CommentSerializer

    class Meta:
        app_label = 'api'
        model = Address
