from django.shortcuts import render_to_response, get_object_or_404
#from django.core.cache import cache
from timelines.models import Timeline

def timeline_index(request, timeline_id):
#    request.session.
#    cache.get('')
    #timeline = Timeline.objects.get(owner = request.session.user)
    timeline = Timeline.objects.get(id=timeline_id)
    post_list = timeline.fresh_posts
    
    return render_to_response('timeline/index.html', {'post_list': post_list}) 
    
def index(request):
    pass
