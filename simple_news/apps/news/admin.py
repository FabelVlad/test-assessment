from django.contrib import admin

from apps.news.models import PostVote, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
    pass
