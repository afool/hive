from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EMOTION_CHOICES = (
        ('H', 'Happy'),
        ('S', 'Sad')
    )

    user = models.OneToOneField(User) # User Profile have to contain this field.
    department = models.CharField(null=True, max_length=50)
    position = models.CharField(null=True, max_length=50)
    emotion = models.CharField(null=True, choices=EMOTION_CHOICES, max_length=20)
    portrait = models.FileField(null=True, upload_to="user_profile/")
    phone = models.CharField(null=True, max_length=50)  

class EmailActivation(models.Model):
    email_address = models.EmailField(unique=True)
    expire_date = models.DateTimeField()
    activation_key = models.CharField(max_length=40)
    #activation_user = models.ForeignKey(User)

class Following(models.Model):
    followee = models.ForeignKey(User, related_name = 'following_followee')
    followee_str = models.CharField(max_length=20, blank=True)
    follower = models.ForeignKey(User, related_name = 'following_follower')
    follower_str = models.CharField(max_length=20, blank=True)
    
    class Meta:
        verbose_name_plural = "Followings"
        ordering = ['followee']
    
    def __unicode__(self):
        return "%s followed by %s" %(self.followee, self.follower)
    
    def save(self, force_insert=False, force_update=False):
        self.followee_str = self.followee.username
        self.follower_str = self.follower.username
        super(Following, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return "/accounts/%s/followings/%d" %(self.followee, self.id)
