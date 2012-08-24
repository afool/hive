from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
    
class Timeline(models.Model):
    LIMIT_OF_FRESH_POSTS = 100
    owner = models.ForeignKey(User)     # timeline's owner
    
    # I hope this ManyToManyField contains foreign_keys of the other table.
    # NOT entire of the data record
    fresh_posts = models.ManyToManyField(Post)
    number_of_fresh_posts = models.IntegerField()
    
    def __unicode__(self):
        return "%s's Timeline" %(self.owner)
    
    def get_absolute_url(self):
        return "/%s/Timeline/" %(self.owner)
        
    def push_post(self, post):
        if self.number_of_fresh_posts >= self.LIMIT_OF_FRESH_POSTS :
            # TO DO : remove oldest fresh posts
            self.number_of_fresh_posts = self.number_of_fresh_posts
        self.fresh_posts.add(post)

