from django.db import models
from django.contrib.auth.models import User

class Hannouncment(models.Model):
    ANNOUNCEMENTS_KINDS = (

    )
    notifier = models.ForeignKey(User)
    notifiee = models.ForeignKey(User, related_name='notification_announcement')
    notificated_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField()
    announcement = models.CharField(max_length=120)
    kinds = models.CharField(choices=ANNOUNCEMENTS_KINDS, max_length=30)

    class Meta:
        pass

    def __unicode__(self):
        pass


class Hmessage(models.Model):
    MESSAGES_KINDS = (

    )

    chater = models.ForeignKey(User)
    chatee = models.ForeignKey(User, related_name='notification_message')
    notificated_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField()
    message = models.CharField(max_length=120)
    kinds = models.CharField(choices=MESSAGES_KINDS, max_length=30)

    class Meta:
        pass

    def __unicode__(self):
        pass

class HRequest(models.Model):
    REQUESTS_KINDS = (

    )

    requester = models.ForeignKey(User)
    requestee = models.ForeignKey(User, related_name='notification_request')
    notificated_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.IntegerField()
    kinds = models.CharField(choices=REQUESTS_KINDS, max_length=30)

    class Meta:
        pass

    def __unicode__(self):
        pass

