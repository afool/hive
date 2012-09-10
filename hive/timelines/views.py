from accounts.models import Following, UserProfile
from posts.models import Like
from timelines.models import Timeline
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse


@login_required(login_url='/accounts/login')
def main_timeline_contents(request,request_timeline_id=None):
    user = request.user
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
                                      'is_maintimeline_active':True,
                                      'is_menu_home':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
        html = html + """<script> var last_timeline_id = %s </script>""" % ( last_timeline_id )
        return HttpResponse(html)
    
    
    return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                      'is_maintimeline_active':True,
                                      'is_menu_home':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id,
                                       }))


@login_required(login_url='/accounts/login')
def profile_timeline_contents(request, username, request_timeline_id=None):
    if request.is_ajax() is True:
        pass
    
    user = User.objects.get(username=username)
    
    if request_timeline_id:
        timelines = Timeline.objects.select_related(depth=1).filter(
            id__lt = request_timeline_id).filter(writer=user).all()[:10]
    else:
        timelines = Timeline.objects.select_related(depth=1).filter(writer=user).all()[:10]
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
                                      'user':user,
                                      'is_menu_profile':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
        html = html + """<script> var last_timeline_id = %s </script>""" % ( last_timeline_id )
        return HttpResponse(html)
    
    return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                      'is_menu_profile':True,
                                      'user': user,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))


@login_required(login_url='/accounts/login')
def humor_timeline_contents(request,request_timeline_id=None):
    user = request.user
    humor_bot = User.objects.get(username="humor_bot")
    
    if request_timeline_id:
        timelines = Timeline.objects.select_related(depth=1).filter(
            id__lt = request_timeline_id).filter(writer=humor_bot).all()[:10]
    else:
        timelines = Timeline.objects.select_related(depth=1).filter(writer=humor_bot).all()[:10]
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
                                      'is_humortimeline_active': True,
                                      'is_menu_home':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
        html = html + """<script> var last_timeline_id = %s </script>""" % ( last_timeline_id )
        return HttpResponse(html)
    
    return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                      'is_humortimeline_active':True,
                                      'is_menu_home':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
    
    
# To Do : humor_timeline_contents , main_timeline_contents, notice_timeline_contents is duplicated code set
#         we can eliminate duplicated code, just merge into one method with parameter (timeline_user)

@login_required(login_url='/accounts/login')
def notice_timeline_contents(request,request_timeline_id=None):
    user = request.user
    notice_bot = User.objects.get(username="notice_bot")
    
    if request_timeline_id:
        timelines = Timeline.objects.select_related(depth=1).filter(
            id__lt = request_timeline_id).filter(writer=notice_bot).all()[:10]
    else:
        timelines = Timeline.objects.select_related(depth=1).filter(writer=notice_bot).all()[:10]
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
                                      'is_noticetimeline_active': True,
                                      'is_menu_home':True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
        html = html + """<script> var last_timeline_id = %s </script>""" % ( last_timeline_id )
        return HttpResponse(html)
    
    return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                      'is_noticetimeline_active':True,
                                      'is_menu_home': True,
                                      'timelines':timelines,
                                      'last_timeline_id' : last_timeline_id }))
    
