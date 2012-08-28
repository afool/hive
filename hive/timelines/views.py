from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from timelines.models import Timeline

def main_timeline_contents(request):
    if request.is_ajax() is True:
        pass
    else:
        contents = Timeline.objects.all()
        return render_to_response('timelines/timeline_view.html', RequestContext(request,{
                                                                                        'contents':contents
                                                                                        }))
