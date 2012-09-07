from django.conf.urls import patterns, include, url

urlpatterns = patterns('timelines.views',
    url(r'^$', 'main_timeline_contents'),
    url(r'^my_timeline/(?P<username>\w+)/$', 'my_timeline_contents'),
    url(r'^get_more_timeline/(?P<request_timeline_id>\d+)/$', 'main_timeline_contents'),
)

