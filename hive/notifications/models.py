from django.db import models
from django.contrib.auth.models import User

class Hannouncment(models.Model):
    ANNOUNCEMENTS_KINDS = (

    )
    notifier = models.ForeignKey(User)
    notifiee = models.ForeignKey(User)
    notificated_time = models.DateTimeField(auto_now_add=True)
    new_announcements = models.IntegerField()
    announcement = models.CharField()
    kinds = models.CharField(choices=ANNOUNCEMENTS_KINDS)

    class __unicode__(self):
        pass

    class Meta:
        ordering = ['notificated_time']


class Hmessage(models.Model):
    MESSAGES_KINDS = (

    )
    notifier = models.ForeignKey(User)
    notifiee = models.ForeignKey(User)
    notificated_time = models.DateTimeField(auto_now_add=True)
    new_announcements = models.IntegerField()
    message = models.CharField()
    kinds = models.CharField(choices=MESSAGES_KINDS)

    class __unicode__(self):
        pass

    class Meta:
        ordering = ['notificated_time']

class HRequest(models.Model):
    REQUESTS_KINDS = (

    )
    requester = models.ForeignKey(User)
    requestee = models.ForeignKey(User)
    notificated_time = models.DateTimeField(auto_now_add=True)
    new_requestments = models.IntegerField()
    kinds = models.CharField(choices=REQUEST_KINDS)

    class __unicode__(self):
        pass

    class Meta:
        ordering = ['notificated_time']


