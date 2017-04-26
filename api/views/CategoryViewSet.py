from rest_framework import viewsets
from api.models import Category
from api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Category.Category.objects.all()
    serializer_class = CategorySerializer

    class Meta:
        app_label = 'api'
        model = Category
