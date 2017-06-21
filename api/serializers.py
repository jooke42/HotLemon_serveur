from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Comment, Topic, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
        
class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ('title', 'author', 'body', 'picture', 'longitude', 'latitude')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category







