from django.conf.urls import patterns, url

urlpatterns = patterns('posts.views',
    url(r"ajax/photos/upload/$", "upload_photos", name="upload_photos"),
    url(r"ajax/photos/recent/$", "recent_photos", name="recent_photos"),
    
    url(r'create/$', 'create_post'),
    url(r'create_comment/(?P<post_id>\d+)/$', 'create_comment'),
    url(r'create_from_timeline/$', 'create_post_timeline'),
    
    url(r'file_upload/','upload_attachments'),
    
    url(r'(?P<post_id>\d+)/$', 'one_of_post_detail'),
    url(r'(?P<post_id>\d+)/on_liked/$', 'on_liked'),
    url(r'(?P<post_id>\d+)/on_unliked/$', 'on_unliked'),   
)
