from django.conf.urls import patterns, url

urlpatterns = patterns('posts.views',
    url(r'(?P<posts_id>\d+)/$', 'one_of_posts_detail'),
    url(r'create/$', 'create_post'),
)
