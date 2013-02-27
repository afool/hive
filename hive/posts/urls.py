from django.conf.urls import patterns, url

urlpatterns = patterns('posts.views',
    url(r'ajax/photos/upload/$', 'upload_photos', name='upload_photos'),
    url(r'ajax/photos/recent/$', 'recent_photos', name='recent_photos'),
    url(r'ajax/post/on_like/(?P<post_id>\d+)/$', 'on_liked'),
    url(r'ajax/post/on_unlike/(?P<post_id>\d+)/$', 'on_unliked'),
    url(r'ajax/post/remove/(?P<post_id>\d+)/$', 'remove'),

    url(r'create_comment/(?P<post_id>\d+)/$', 'create_comment'),
    url(r'create_from_timeline/$', 'create_post_timeline'),

    url(r'file_upload/','upload_attachments'),

    url(r'(?P<post_id>\d+)/$', 'one_of_post_detail'),
)
