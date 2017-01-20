from django.contrib import admin
from api.models.News import News
from api.models.Topic import Topic
from api.models.Comment import Comment


class CommentAdmin(Comment):
    pass


class TopicAdmin(Topic):
    pass


class NewsAdmin(News):
    pass
