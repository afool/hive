from django.conf.urls import patterns, include, url

import django.contrib.auth

urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'email_register_page'),

    url(r'^info/(\w+)/$', 'userinfo_page'),
    #url(r'login/$', 'login_page'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^followlist/$', 'followlist_page'),
    url(r'^addfollow/$', 'addfollow_page'),
    url(r'^finduser/$', 'finduser_page'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
)
