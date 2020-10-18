from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.news.views import PostViewSet, CommentViewSet

app_name = 'news'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
