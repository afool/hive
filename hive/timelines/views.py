from accounts.models import Following, UserProfile
from posts.models import Like
from timelines.models import Timeline
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse


@login_required(login_url='/accounts/login')
def main_timeline_contents(request,request_timeline_id=None):
    user = request.user
    user_profile = UserProfile.objects.get(user = user)
    if request_timeline_id:
        timelines = Timeline.objects.select_related(depth=1).filter(
            id__lt = request_timeline_id).filter(
            writer__in = Following.objects.filter(follower=user).values("followee")
                    ).all()[:10]
    else:
        timelines = Timeline.objects.select_related(depth=1).filter(
            writer__in = Following.objects.filter(follower=user).values("followee")
                    ).all()[:10]
        # at first load 10
    # leave a flag whether current user liked this post
    last_timeline_id = 0
    for timeline in timelines:
        timeline.is_liked = False
        if timeline.post.is_liked_by_observer(user):
            timeline.is_liked = True
        last_timeline_id = timeline.id
    if request_timeline_id:
        # render partial
        html = render_to_string('timelines/timeline_timeline.html', RequestContext(request,{
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
        html = html + """<script> var last_timeline_id = %s </script>""" % ( last_timeline_id )
        return HttpResponse(html)


    return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))

@login_required(login_url='/accounts/login')
def my_timeline_contents(request):
    if request.is_ajax() is True:
        pass
    
    user = request.user
    timelines = Timeline.objects.select_related(depth=1).filter(
                                        writer = user
                                        ).all()   

    for timeline in timelines:
        timeline.is_liked = False
        if timeline.post.is_liked_by_observer(user):
            timeline.is_liked = True
    return render_to_response('timelines/mytimeline_view.html', RequestContext(request,{
                                                                                        'timelines':timelines,
                                                                                        'user': user,
                                                                                        }))
