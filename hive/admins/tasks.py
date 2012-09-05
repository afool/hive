from admins.models import ActivitiesInformation
from celery import task
from posts.models import Post, Like, Comment

import datetime

@task(name='execute_analyze_activities')
def execute_analyze_activities():
    num_of_posts = Post.objects.all().count()
    num_of_likes = Like.objects.all().count()
    num_of_comments = Comment.objects.all().count()
    
    ActivitiesInformation.objects.create(date = datetime.datetime.today(),
                                         num_posts = num_of_posts,
                                         num_likes = num_of_likes,
                                         num_comments = num_of_comments,
                                         num_web_feeds = 0,
                                         num_messages = 0,
                                          )
    excute_again()
    execute_analyze_activities.name
    
def excute_again():
    execute_analyze_activities.apply_async(countdown=3)


