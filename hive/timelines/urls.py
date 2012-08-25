from django.conf.urls import patterns, include, url

urlpatterns = patterns('timelines.views',
    url(r'^$', 'main_timeline_contents'),
    url(r'^get_more_timeline/(?P<last_posts_id>\d+)$', 'get_more_timeline_contents'),
)

