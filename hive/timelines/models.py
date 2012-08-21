from django.db import models
from django.contrib.auth.models import User

class Timeline(models.Model):
    
    owner = models.ForeignKey(User)     # timeline's owner
    following_list = models.ManyToManyField(User)
    
