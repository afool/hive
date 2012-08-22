from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admins/', include('admins.urls')),
    url(r'^chats/', include('chats.urls')),
    url(r'^hgroups/', include('hgroups.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^timelines/', include('posts.urls')),
)

