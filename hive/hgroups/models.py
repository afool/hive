from django.db import models
from django.contrib.auth.models import User

class GroupProfile(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200)
    gimage = models.FileField(null=True, upload_to="group_profile/")
    create_time = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField()

    members = models.ManyToManyField(User, through='Membership')

    class Meta:
        pass

    def __unicode__(self):
        pass

class Membership(models.Model):
    LEVEL_OWNER = 0
    LEVEL_MEMBER = 1
    LEVEL_CHOICES = (
                    (LEVEL_OWNER, 'owner'),
                    (LEVEL_MEMBER, 'member'),
                   )

    person = models.ForeignKey(User)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    group = models.ForeignKey(GroupProfile)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __unicode__(self):
        pass
