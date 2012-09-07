from django.conf.urls import patterns, include, url

urlpatterns = patterns('timelines.views',
    url(r'^$', 'main_timeline_contents'),
    url(r'^my_timeline/$', 'my_timeline_contents'),
    url(r'^humor_timeline/$', 'humor_timeline_contents'),
    url(r'^humor_timeline/(?P<request_timeline_id>\d+)/$', 'humor_timeline_contents'),
    url(r'^get_more_timeline/(?P<request_timeline_id>\d+)/$', 'main_timeline_contents'),
)

