from django.db import models
from django.contrib.auth.models import User

#from timelines.models import FollowerList, Timeline

class Post(models.Model):
    contents = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)
    author = models.CharField(max_length=100)
    has_attachments = models.BooleanField()
    comments_count = models.IntegerField()
    like_count = models.IntegerField()
    like_string = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-create_time']
    
    def __unicode__(self):
        return "Post by %s" %(self.author)
    
    def save(self, force_insert=False, force_update=False):
        self.author = self.writer.username
        super(Post, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return "/posts/author/%d/" %(self.id)

class Attachment(models.Model):
    file_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    contents_file = models.FileField(upload_to="attachments/")
    post = models.ForeignKey(Post)
    
    class Meta:
        verbose_name_plural = "Attachments"
        ordering = ['-create_time']
    
    def __unicode__(self):
        return "Attachment of %s" %(self.post)
        
    def get_absolute_url(self):
        return "/posts/attachments/%d" %(self.id)


class Comment(models.Model):
    comments = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    
    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-create_time']
    
    def __unicode__(self):
        return "Comment by %s" %(self.author)
    
    def save(self, force_insert=False, force_update=False):
        self.author = self.writer.username
        super(Comment, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return "/posts/comments/%d/" %(self.id)


class Like(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    liker = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    class Meta:
        verbose_name_plural = "Likes"
        ordering = ['-create_time']
    
    def __unicode__(self):
        return "Like by %s" %(self.liker)
        
    def get_absolute_url(self):
        return "/posts/likes/%d/" %(self.id)
