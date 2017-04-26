from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Users to be viewed or edited.
        """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        app_label = 'api'
        model = User
