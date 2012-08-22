from django.conf.urls import patterns, include, url

urlpatterns = patterns('timeline.views',
    url(r'^$', 'index'),
)
