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
    expired_date = models.DateTimeField()
    activation_key = models.CharField(max_length=40)
    activation_user = models.ForeignKey(User)
