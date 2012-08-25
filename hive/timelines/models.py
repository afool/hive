from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Followers(models.Model):
    follower = models.ForeignKey(User)
    followee = models.ForeignKey(User, related_name='timelines_followers')

class Timeline(models.Model):
    author = models.ForeignKey(User)
    content = models.ForeignKey(Post)

    def get_comment_count(self):
        comments = Comment.objects.filter(post=self.content)
        return len(comments)
