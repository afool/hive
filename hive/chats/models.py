from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):

    sender = models.ForeignKey(User, related_name='message_sender')
    receiver = models.ForeignKey(User, related_name='message_receiver')
    message = models.CharField(max_length=500)
    write_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['write_time']

    def __unicode__(self):
        pass


