from rest_framework import viewsets
from api.models import Comment
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Comment.Comment.objects.all()
    serializer_class = CommentSerializer

    class Meta:
        app_label = 'api'
        model = Comment
