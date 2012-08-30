from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models import F

#from timelines.models import FollowerList, Timeline

class Post(models.Model):
    STR_NOBODY_LIKE = "be the first one likes this post"
    STR_SOMEONE_LIKE = "%s likes this post"
    STR_SOMEBODIES_LIKE = "%s and some others like this post"
    
    contents = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)
    author = models.CharField(max_length=100, null=True)
    has_attachments = models.BooleanField(default=False)
    comments_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    like_string = models.CharField(max_length=100, default=STR_NOBODY_LIKE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-id']
    
    def __unicode__(self):
        return "Post by %s" %(self.author)
        
    def get_absolute_url(self):
        return "/posts/%d/" %(self.id)
    
    def get_rendered(self):
        return render_to_string('posts/post_render.html', {'post':self})
    
    def on_liked(self, like_user):
        self.like_count = F('like_count')+1
        self.update_like_string(like_user.username)
        self.save()
    
    def on_unliked(self):
        self.like_count = F('like_count')-1
        like = Like.objects.get(post=self)
        self.update_like_string(like.liker.username)
        self.save()
    
    def update_like_string(self, author):
        if self.like_count is 0:
            self.like_string = self.STR_NOBODY_LIKE
        elif self.like_count is 1:
            self.like_string = self.STR_SOMEONE_LIKE %(author)
        else:
            self.like_string = self.STR_SOMEBODIES_LIKE %(author)
       

class Attachment(models.Model):
    file_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    contents_file = models.FileField(upload_to='attachments/')
    post = models.ForeignKey(Post)
    class Meta:
        verbose_name_plural = "Attachments"
        ordering = ['-id']
    
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
        ordering = ['-id']
    
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
        ordering = ['-id']
        unique_together = ("liker", "post")
    
    def __unicode__(self):
        return "Like by %s" %(self.liker)
        
    def get_absolute_url(self):
        return "/posts/likes/%d/" %(self.id)
