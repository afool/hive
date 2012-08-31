from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('accounts.views',
    url(r'^register_email/$', 'email_register_page'),
    url(r'^activate_email/(?P<key>\w+)/$', 'activation_page'),
    url(r'^register_userinfo/$', 'register_userinfo_page'),
    url(r'^forgot_password/$', direct_to_template, {'template': 'accounts/forgot_password.html'}),
    url(r'^renew_password_email/(?P<key>\w+)/$', 'renew_password_page'),
    url(r'^reset_password/$', 'reset_password_page'),


    #url(r'login/$', 'login_page'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^people_list/$', 'people_list_page'),
    url(r'^profile/(?P<username>\w+)/$', 'profile_page'),
    url(r'^addfollow/(?P<followee_id>\d+)/(?P<follower_id>\d+)/$', 'add_follow_page'),
    url(r'^finduser/$', 'finduser_page'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
)
