from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, Comment

class Timeline(models.Model):
    author = models.ForeignKey(User)
    content = models.ForeignKey(Post)

    def get_comment_count(self):
        comments = Comment.objects.filter(post=self.content)
        return len(comments)
