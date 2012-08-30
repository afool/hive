from django.conf.urls import patterns, url

urlpatterns = patterns('posts.views',
    url(r'(?P<post_id>\d+)/$', 'one_of_post_detail'),
    url(r'(?P<post_id>\d+)/on_liked/$', 'on_liked'),
    url(r'(?P<post_id>\d+)/on_unliked/$', 'on_unliked'),
    url(r'create/$', 'create_post'),
    url(r'create_from_timeline/$', 'create_post_timeline'),
)
