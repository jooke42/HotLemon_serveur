"""hotlemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api.models.Topic import Topic
from api.models.News import News
from api.models.Comment import Comment
import api.views
import hotlemon.settings

router = routers.DefaultRouter()
router.register(r'users', api.views.UserViewSet)
router.register(r'groups', api.views.GroupViewSet)
router.register(r'topics', api.views.TopicViewSet)
router.register(r'comments', api.views.CommentViewSet)
router.register(r'categories', api.views.CategoryViewSet)
router.register(r'news', api.views.NewsViewSet)
admin.site.register(Topic)
admin.site.register(News)
admin.site.register(Comment)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': hotlemon.settings.MEDIA_ROOT, 'show_indexes': False}),

]

