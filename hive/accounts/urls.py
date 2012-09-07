from django.conf.urls import include, patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('accounts.views',
    url(r'^activate_email/(?P<key>\w+)/$', 'activation_page'),
    url(r'^addfollow/(?P<followee_id>\d+)/$', 'add_follow_page'),
    
    url(r'^forgot_password/$', direct_to_template, {'template': 'accounts/forgot_password.html'}),
    url(r'^forgot_password_send/$', 'forgot_password_page'),
    
    url(r'^register_email/$', 'email_register_page'),    
    url(r'^register_userinfo/(?P<key>\w+)/$', 'register_userinfo_page'),
    url(r'^removefollow/(?P<followee_id>\d+)/$', 'remove_follow_page'),
    url(r'^renew_password_email/(?P<key>\w+)/$', 'renew_password_email_page'),
    url(r'^renew_password/(?P<key>\w+)$', 'renew_password_page'),
    
    url(r'^people_list/$', 'people_list_page'),
    url(r'^profile/$', 'profile_page'), # just display current user's profile
    url(r'^profile/(?P<username>\w+)/$', 'profile_page'),
    
    url(r'^update_profile/$', 'update_profile_page'),
    url(r'^update_profile_save/$', 'update_profile_save_page'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
)