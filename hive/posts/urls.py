from django.conf.urls import patterns, include, url

from hive.posts.views import one_of_posts_detail

urlpatterns = patterns('',
    url(r'posts/(\d+)/$', one_of_posts_detail),
)
