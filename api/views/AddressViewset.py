from rest_framework import viewsets
from api.models import Address
from api.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    class Meta:
        app_label = 'api'
        model = Address
