from django.conf.urls import patterns, include, url

urlpatterns = patterns('admins.views',
    url(r'^$', 'index'),
)
