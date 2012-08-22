from django.conf.urls import patterns, include, url

urlpatterns = patterns('notifications.views',
    url(r'^$', 'index'),
)
