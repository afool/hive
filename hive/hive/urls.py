from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, { 'template': 'main/index.html' }),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admins/', include('admins.urls')),
    url(r'^chats/', include('chats.urls')),
    url(r'^hgroups/', include('hgroups.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^timelines/', include('timelines.urls')),
)

