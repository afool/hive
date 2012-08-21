from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class FollowerList(models.Model):
    
    owner = models.OneToOneField(User)
    followers = models.ManyToManyField(User)
    
    def __unicode__(self):
        return "%s's FollowerList" %(self.owner)
    
    def get_absolute_url(self):
        return "/%s/follower_list/" %(self.owner)
    
    def on_new_follower(self, newFollower):
        self.followers.add(newFollower)
        pass
    
    def on_add_post(self, post):
        for follower in self.followers:
            follower_timeline = Timeline.objects.get(owner = follower.owner)
            follower_timeline.push_post(post)


class Timeline(models.Model):
    
    LIMIT_OF_FRESH_POSTS = 100
    owner = models.ForeignKey(User)     # timeline's owner
    following_list = models.ManyToManyField(User)
    
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

    