from django.core.management.base import BaseCommand

from accounts.models import UserProfile
from django.contrib.auth.models import User
from admins.tasks import execute_analyze_activities, excute_post_humorbot
from posts.models import Post
from timelines.models import Timeline
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.get(username="notice_bot")
            print "Notice Bot is exist"
        except User.DoesNotExist:
            notice_bot = User.objects.create_user("notice_bot", "notice_bot@test.com", "notice_bot")
            notice_bot.is_active=True
            notice_bot.is_staff = True
            notice_bot.is_superuser = True
            notice_bot.save()
            UserProfile.objects.create(user=notice_bot)
            
            now = datetime.datetime.now()
            post_content = "WELCOME TO HIVE!"
            now = now + datetime.timedelta(minutes=1)
            post = Post.objects.create( contents=post_content, create_time=now, writer=notice_bot, author=notice_bot.username)
            Timeline.objects.create( writer=notice_bot, post=post )
            print "Notice Bot(%s) is Created" %(notice_bot)
        
        try:
            User.objects.get(username="humor_bot")
            print "Humor Bot is exist"
        except User.DoesNotExist:
            humor_bot = User.objects.create_user("humor_bot" , "humor_bot@test.com", "humor_bot")
            humor_bot.is_active=True
            humor_bot.is_staff = True
            humor_bot.is_superuser = True
            humor_bot.save()
            UserProfile.objects.create(user=humor_bot)
            print "Humor Bot(%s) is created" %(humor_bot)
        
                
        execute_analyze_activities()
        print "Activities Analyzer is excuted."
        
        excute_post_humorbot()
        print "Humor Bot is running"
        
        print "Initialize Completed"

