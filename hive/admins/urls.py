from django.conf.urls import patterns, url

urlpatterns = patterns('admins.views',
    url(r'^$', 'main'),

    url(r'^activities/$', 'activities_overview'),
    url(r'^activities/(?P<year>\d{4})(?P<month>\w{3})(?P<day>\d{2})/$', 'activities_detail'),

    url(r'^customize/(?P<customize_id>\d+)/$', 'customize_detail'),
    
    url(r'^trend/$', 'trend_overview'),
    url(r'^trend/(?P<year>\d{4})(?P<month>\w{3})(?P<day>\d{2})/$', 'trend_detail'),

    url(r'^user/$', 'control_user'),
    url(r'^(\w+)/$', 'analytics_detail'),

    url(r'^user/(\w+)/(\w+)/$', 'ban_and_staff'),
)
