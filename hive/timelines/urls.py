from django.conf.urls import patterns, include, url

urlpatterns = patterns('timelines.views',
    url(r'^$', 'index'),
    url(r'^(?P<timeline_id>\d+)/$', 'timeline_index')
)

