from django.db import models
from posts.models import Post

# daily activities
class ActivitiesInformation(models.Model):
    date = models.DateField()
    num_posts = models.IntegerField(default =0)
    num_likes = models.IntegerField(default = 0)
    num_comments = models.IntegerField(default = 0)
    num_web_feeds = models.IntegerField(default =0)
    num_messages = models.IntegerField(default =0)
    
    class Meta:
        verbose_name_plural = "ActivitiesInformations"
        ordering = ['date']    # like a query option ORDER BY date DESC
    
    def __unicode__(self):
        return "Activities of %s" %(self.date)
    
    def get_absolute_url(self):
        return "/admins/activities/%s/" %(self.date.strftime("%Y%b%d").lower())
    
    def on_new_posts(self):
        pass


class CustomizeInformation(models.Model):
    THEME_DEFAULT = 0
    THEME_1 = 1
    THEME_2 = 2
    THEME_CHOICES = (
                     (THEME_DEFAULT, "DEFAULT_THEME"),
                     (THEME_1, "THEME_1"),
                     (THEME_2, "THEME_2")
                     )
    
    logo_file_name = models.CharField(max_length=100)
    logo_file = models.FileField(upload_to="customize_info/")
    theme = models.IntegerField(choices = THEME_CHOICES, default = THEME_DEFAULT)
    default_profile_picture = models.FileField(upload_to="customize_info/")
    
    def __unicode__(self):
        return "CustomizeInformation"
    
    def get_absolute_url(self):
        return "/admins/customize/%d/" %(self.id)


# Event - Event Management System
class Event(models.Model):
    pass


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

    def calculate_total_points(self):
        return self.num_comments + self.num_likes
        
    def save(self, force_insert=False, force_update=False):
        self.total_points = self.calculate_total_points() 
        super(Trend, self).save(force_insert, force_update)
 
    
    def get_absolute_url(self):
        return "/admins/trend/%s/" %(self.date.strftime("%Y%b%d").lower())
