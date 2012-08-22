from django.conf.urls import patterns, include, url

urlpatterns = patterns('chats.views',
    url(r'^$', 'index'),
)
