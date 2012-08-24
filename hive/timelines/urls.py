from django.conf.urls import patterns, include, url

from hive.timelines import main_timeline_contents, get_more_timeline_contents

urlpatterns = patterns('timelines.views',
    url(r'^$', main_timeline_contents),
    url(r'^get_more_timeline/$', get_more_timeline_contents),
)

