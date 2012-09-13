from django.core.management.base import BaseCommand

from accounts.models import UserProfile
from django.contrib.auth.models import User
from posts.models import Post
from timelines.models import Timeline
import random
import datetime



class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() < 5 :
            for x in range(100):
                user = User.objects.create_user("test" + str(x), "test" + str(x) + "@test.com", "test"+str(x))
                UserProfile.objects.create( user = user )
                print "User(%s) is created" %(user)
            print "Test Users are created"
            
            for x in range(10):
                exclude_list=("humor_bot","notice_bot")
                now = datetime.datetime.now()
                users = User.objects.order_by("?").all().exclude(username__in=exclude_list)
                for user in users:
                    post_content = "let's play HIVE! %d" %(random.randint(0,100000))
                    now = now + datetime.timedelta(minutes=1)
                    post = Post.objects.create( contents = post_content , create_time = now , writer = user , author = user.username)
                    Timeline.objects.create( writer = user , post = post )
                    print "Post(%s) is created" %(post)
            print "Test Timeline are created"