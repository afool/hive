from django.conf.urls import patterns, include, url

urlpatterns = patterns('posts.views',
    url(r'^$', 'index'),
)
