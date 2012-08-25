from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'register_page'),

    url(r'^info/(\w+)/$', 'userinfo_page'),
    url(r'^settings/$', 'settings_page'),
    url(r'^followlist/$', 'follows_page'),
    url(r'^finduser/$', 'finduser_page'),
    url(r'^logout/$', 'logout_page'),
)
