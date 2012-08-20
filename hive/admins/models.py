from django.contrib.auth.models import User
from django.db import models
from posts.models import Post

# daily activities
class ActivitiesInformation(models.Model):
    
    date = models.DateField()
    num_likes = models.IntegerField(default = 0)
    num_comments = models.IntegerField(default = 0)
    num_web_feeds = models.IntegerField(default =0)
    num_messages = models.IntegerField(default =0)
    
    class Meta:
        verbose_name_plural = "ActivitiesInformations"
        ordering = ['-date']    # like a query option ORDER BY date DESC
    
    def __unicode__(self):
        return "Activities of %s" %(self.date)
    
    def get_absolute_url(self):
        return "/admins/ActivitiesInformation/%s/" %(self.date.strftime("%Y%b%d").lower())


# daily activities
class Trend(models.Model):
    
    date = models.DateField()
    post = models.ForeignKey(Post)
    num_comments = models.IntegerField()
    num_likes = models.IntegerField()
    total_points = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Trends"
        ordering = ['-date']
    
    def __unicode__(self):
        return "Trend of %s" %(self.date)
    
    def get_absolute_url(self):
        return "/admins/Trend/%s/" %(self.date.strftime("%Y%b%d").lower())



class CustomizeInformation(models.Model):
    
    THEME_DEFAULT = 0
    THEME_1 = 1
    THEME_2 = 2
    THEME_CHOICES = (
                     (THEME_DEFAULT, "DEFAULT_THEME"),
                     (THEME_1, "THEME_1"),
                     (THEME_2, "THEME_2")
                     )
    
    logo_file_name = models.CharField()
    logo_file = models.FileField()
    theme = models.IntegerField(choices = THEME_CHOICES, default = THEME_DEFAULT)
    default_profile_picture = models.FileField()
    
    def __unicode__(self):
        return "CustomizeInformation"
    
    def get_absolute_url(self):
        return "/admins/CustomizeInformation/"

# Event - Event Management System
class Event(models.Model):
    pass
