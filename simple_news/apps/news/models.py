from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link = models.URLField(help_text='max lenght 200 char')
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=1800, unique=True)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return f'comment on {self.post} by {self.author_name}'


class PostVote(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postvotes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postvotes')

    def __str__(self):
        return f'vote on {self.post} by {self.author_name}'
