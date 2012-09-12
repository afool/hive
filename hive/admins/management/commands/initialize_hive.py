from django.core.management.base import BaseCommand

from accounts.models import UserProfile
from django.contrib.auth.models import User
from admins.tasks import execute_analyze_activities, excute_post_humorbot


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.get(username="notice_bot")
            print "Notice Bot is exist"
        except User.DoesNotExist:
            notice_bot = User.objects.create_user("notice_bot", "notice_bot@test.com", "notice_bot")
            UserProfile.objects.create(user=notice_bot)
            print "Notice Bot(%s) is Created" %(notice_bot)
        
        try:
            User.objects.get(username="humor_bot")
            print "Humor Bot is exist"
        except User.DoesNotExist:
            humor_bot = User.objects.create_user("humor_bot" , "humor_bot@test.com", "humor_bot")
            UserProfile.objects.create(user=humor_bot)
            print "Humor Bot(%s) is created" %(humor_bot)
            
        
        execute_analyze_activities()
        print "Activities Analyzer is excuted."
        
        excute_post_humorbot()
        print "Humor Bot is running"
        
        print "Initialize Completed"

