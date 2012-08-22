from django.conf.urls import patterns, include, url

urlpatterns = patterns('hgroups.views',
    url(r'^$', 'index'),
)
