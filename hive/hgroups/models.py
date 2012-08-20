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
    create_time = models.DataTimeField(auto_now_add=True)

class UserList(models.Model):
    hgroup = models.ForeignKey(GroupProfile)
    users = models.ManyToManyField(User)

