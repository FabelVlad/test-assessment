from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.news.models import PostVote, Post, Comment
from apps.news.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    @method_decorator(login_required(login_url='api-auth:login'))
    @action(detail=True, methods=['get'])
    def vote(self, request, **kwargs):
        post = self.get_object()
        user = self.request.user
        obj, created = PostVote.objects.get_or_create(post=post, author_name=user)
        if not created:
            obj.delete()
            return Response({'status': 'unvoted'})
        return Response({'status': 'voted'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)


def redirect_to_api_root(request):
    return redirect('/api/v1/', permanent=True)
