from admins.models import ActivitiesInformation
from celery import task
from posts.models import Post, Like, Comment
from timelines.models import Timeline
from django.contrib.auth.models import User
from utilities.dogdrip_crawler import get_contents_from_post, get_post_list 
import datetime

ANALYZING_PERIOD = 30
HUMOR_BOT_PERIOD = 20

@task(name='execute_analyze_activities')
def execute_analyze_activities():
    def _excute_again():
        execute_analyze_activities.apply_async(countdown=ANALYZING_PERIOD)
    
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
    _excute_again()
    execute_analyze_activities.name

@task(name='excute_post_humorbot')
def excute_post_humorbot():
    def _excute_again():
        excute_post_humorbot.apply_async(countdown=HUMOR_BOT_PERIOD)
    
    post_url_list = get_post_list()
    if len(post_url_list) is 0:
        _excute_again()
        return
    
    user_bot = User.objects.get(username="humor_bot")
    count = 0
    for post_url in post_url_list:
        if count >= 5:
            break
        count += 1
        content = get_contents_from_post(post_url=post_url)
        post = Post.objects.create(contents=content, writer=user_bot, author=user_bot.username)
        Timeline.objects.create(post=post, writer=post.writer)
    
    _excute_again()
    return

