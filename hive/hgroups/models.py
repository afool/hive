from django.db import models
from django.contrib.auth.models import User

class GroupProfile(models.Model):
    GROUP_KINDS = (
        ('MU', 'Music'),
        ('IT', 'Information Technology'),
    )

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    owner_str = models.CharField(max_length=50)
    gimage = models.FileField(null=True, upload_to="group_profile/")
    kinds = models.CharField(choices=GROUP_KINDS, max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField()

    members = models.ManyToManyField(User, through='Membership', related_name="group_members")

    class Meta:
        pass

    def __unicode__(self):
        pass

class Membership(models.Model):
    person = models.ForeignKey(User)
    group = models.ForeignKey(GroupProfile)
    date_joined = models.DateField()

    class Meta:
        pass

    def __unicode__(self):
        pass
