from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'timelines.views.main_timeline_contents'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admins/', include('admins.urls')),
    url(r'^hgroups/', include('hgroups.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^timelines/', include('timelines.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG is True:
    """ for development serving assets """
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
