from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'email_register_page'),

    url(r'^info/(\w+)/$', 'userinfo_page'),
    url(r'login/$', 'login_page'),

    url(r'^followlist/$', 'followlist_page'),
    url(r'^addfollow/$', 'addfollow_page'),
    url(r'^finduser/$', 'finduser_page'),
    url(r'^logout/$', 'logout_page'),
)
