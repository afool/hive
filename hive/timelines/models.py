from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Followers(models.Model):
    follow_user = models.ForeginKey(User)
    followed_user = models.ForeginKey(User)

class Timeline(models.Modlel):
    author = models.ForeginKey(User)
    content = models.ForeginKey(Post)

    def get_comment_count(self):
        comments = Comment.objects.filter(post=self.content)
        return len(comments)
