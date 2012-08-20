from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    sender = models.ForeignKey(User)
    recevier = models.ForeignKey(User)
    message = models.CharField()
    write_time = models.DateTimeField(auto_now_add=True)
