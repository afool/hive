from django.conf.urls import patterns, include, url

urlpatterns = patterns('timelines.views',
    url(r'^$', 'main_timeline_contents'),
    url(r'^profile_timeline/(?P<username>\w+)/$', 'profile_timeline_contents'),
    url(r'^profile_timeline/(?P<username>\w+)/(?P<request_timeline_id>\d+)/$', 'profile_timeline_contents'),
    url(r'^humor_timeline/$', 'humor_timeline_contents'),
    url(r'^humor_timeline/(?P<request_timeline_id>\d+)/$', 'humor_timeline_contents'),
    url(r'^notice_timeline/$', 'notice_timeline_contents'),
    url(r'^notice_timeline/(?P<request_timeline_id>\d+)/$', 'notice_timeline_contents'),
    url(r'^get_more_timeline/(?P<request_timeline_id>\d+)/$', 'main_timeline_contents'),
)

