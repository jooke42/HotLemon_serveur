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
from api.models import *

from api.views.UserViewSet import UserViewSet
from api.views.GroupViewSet import GroupViewSet
from api.views.TopicViewSet import TopicViewSet
from api.views.CommentViewSet import CommentViewSet
from api.views.CategoryViewSet import CategoryViewSet
from api.views.NewsViewSet import NewsViewSet
from api.views.AddressViewset import AddressViewSet
from api.views.EventViewSet import EventViewSet
import hotlemon.settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'address', AddressViewSet)
router.register(r'events', EventViewSet)
admin.site.register(Topic)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Category)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': hotlemon.settings.MEDIA_ROOT, 'show_indexes': False}),

]

