from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, Comment

class Timeline(models.Model):
    writer = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    class Meta:
        verbose_name_plural = "Timelines"
        ordering = ['-id']
    
    def __unicode__(self):
        return "Timeline #%d by %s" %(id, self.writer)
        
    def get_absolute_url(self):
        #posts/(?P<posts_id>\d+)/$
        return "/timeline/%d/" %(self.id)
