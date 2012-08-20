from django.db import models
from django.contrib.auth.models import User

class GroupProfile(models.Model):
    GROUP_KINDS = (
        ('MU', 'Music'),
        ('IT', 'Information Technology'),
    )

    name = models.CharField()
    owner = models.CharField()
    gimage = models.ImageField(null=True)
    kinds = models.CharField(choices=GROUP_KINDS)
    create_time = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField()
    
    members = models.ManyToManyField(User, through='Membership')

class Membership(models.Model):
    person = models.ForeignKey(User)
    group = models.ForeignKey(GroupProfile)
    date_joined = models.DateField()
