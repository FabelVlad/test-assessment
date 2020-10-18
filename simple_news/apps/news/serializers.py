from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.news.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:post-detail', lookup_field='pk')
    is_voted = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('url', 'title', 'link', 'amount_of_upvotes', 'creation_date', 'is_voted',)
        read_only_fields = ['amount_of_upvotes']

    def get_is_voted(self, obj: Post) -> bool:
        user = self.context.get('request').user
        if isinstance(user, AnonymousUser):
            return False
        else:
            return obj.postvotes.filter(author_name=self.context.get('request').user).exists()


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:comment-detail', lookup_field='pk')

    class Meta:
        model = Comment
        exclude = ('url', 'author_name', 'id',)
