from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from timelines.models import Timeline

@login_required(login_url='/accounts/login')
def main_timeline_contents(request):
    if request.is_ajax() is True:
        pass
    else:
        timelines = Timeline.objects.all()
        
        # leave a flag whether current user liked this post
        for timeline in timelines:
            timeline.is_liked = False
            if timeline.post.is_liked_by_observer(request.user):
                timeline.is_liked = True
        return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                                                                        'timelines':timelines
                                                                                        }))
