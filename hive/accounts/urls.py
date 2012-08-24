from django.conf.urls import patterns, include, url

# Almost same as facebook
urlpatterns = patterns('accounts.views',
    url(r'^info/$', 'user_information'),
)
