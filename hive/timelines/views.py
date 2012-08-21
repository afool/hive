from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Post
from django.core.cache import cache

def timeline_index(request):
#    request.session.
#    cache.get('')
    post_list = Post.objects.order_by('create_time')[:5]
    return render_to_response('timeline/index.html', 
                              {'post_list': post_list})

