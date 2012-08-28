# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Post
from timelines.models import Timeline
from django.http import Http404, HttpResponseRedirect
from forms import PostForm
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
    pass

def one_of_posts_detail(request, posts_id):
    try:
        post = Post.objects.get(id = posts_id)
    except Post.DoesNotExist:
        raise Http404
    
    return render_to_response('posts/post_detail.html', RequestContext(request, {
                             'post': post
                            }))

def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        post = post_form.save()
        Timeline.objects.create(content=post)
        return HttpResponseRedirect(post.get_absolute_url())
    form = PostForm()
    
    return render_to_response('posts/post_create.html', RequestContext(request,
                              {
                               'form':form,
                               },))


