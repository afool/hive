from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EMOTION_CHOICES = (
        ('H', 'Happy'),
        ('S', 'Sad')
    )

    department = models.CharField(null=True)
    position = models.CharField(null=True)
    emotion = models.CharField(null=True, choices=EMOTION_CHOICES)
    portrait = models.ImageField(null=True)
    phone = models.CharField(null=True)
    user = models.ForeignKey(User)

class EmailActivation(models.Model):
    expired_date = models.DateTimeField()
    activation_key = models.CharField(max_length=40)
    activation_user = models.ForeignKey(User)
