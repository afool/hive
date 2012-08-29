# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post
from timelines.models import Timeline
from django.http import Http404, HttpResponseRedirect
from forms import PostForm
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

@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        post = post_form.save(commit=False)
        if request.user.is_authenticated() is False:
            return HttpResponseRedirect('/accounts/login')
        post.writer = request.user
        post.save()
        
        Timeline.objects.create(post=post, writer=post.writer)
        return HttpResponseRedirect(post.get_absolute_url())
    form = PostForm()
    
    return render_to_response('posts/post_create.html', RequestContext(request,
                              {
                               'form':form,
                               },))


