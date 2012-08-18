from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    contents = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)
    author = models.CharField()
    has_attachments = models.BooleanField()
    comments_count = models.IntegerField()
    like_count = models.IntegerField()
    like_string = models.CharField()

class Attachments(models.Model):
    file_name = models.CharField()
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField()
    contents_file = models.FileField()
    post = models.ForeignKey(Post)

class Comments(models.Model):
    comments = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)
    author = models.CharField()
    post = models.ForeignKey(Post)

class Like(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    liker = models.Foreignkey(User)
    post = models.ForeignKey(Post)
