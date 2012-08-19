from django.contrib.auth.models import User
from django.db import models

# Bot - Automatic Posting System 
#     - upload the post at scheduled dated
#     - BotContent.writer is the author, a.k.a. Bot
class BotContent(models.Model):
    
    scheduled_upload_time = models.DateTimeField(null=False)
    contents = models.TextField()
    writer = models.ForeignKey(User)    # user or  Bot Class
    writer_str = models.CharField()
    has_attachments = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "BotContents"
        ordering = ['scheduled_upload_time']    # like a query option ORDER BY pub_date DESC
    
    def __unicode__(self):
        return "%s/%s" %(self.writer, self.scheduled_upload_time.strftime("%Y%b%d").lower())
    
    def get_absolute_url(self):
        return "/admin/bot/%s/%s/" %(self.writer_str, self.scheduled_upload_time.strftime("%Y%b%d").lower())


class BotContentAttachment(models.Model):
    
    file_name = models.CharField()
    description = models.CharField()
    contents_file = models.FileField()
    botContent = models.ForeignKey()
    
    class Meta:
        verbose_name_plural = "BotContentAttachments"
    
    def __unicode__(self):
        return self.file_name
    
    def get_absolute_url(self):
        return "%s/%s/" %(self.botContent.get_absolute_url(), self.file_name)

# Event - Event Management System
class Event(models.Model):
    pass
