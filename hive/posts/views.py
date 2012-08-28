# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from posts.models import Post
from django.http import Http404, HttpResponseRedirect
from forms import PostForm
from django.core.urlresolvers import reverse


def index(request):
    pass

def one_of_posts_detail(request, posts_id):
    try:
        post = Post.objects.get(id = posts_id)
    except Post.DoesNotExist:
        raise Http404
    
    return render_to_response('posts/post_detail.html', post)

def create_post(request):
    if request.method == "POST":
        post = PostForm(request.Post)
        post.save()
        
        return HttpResponseRedirect(reverse('posts:one_of_post_detail', args=[post.id]))
    form = PostForm()
    
    return render_to_response('posts/post_create.html', 
                              {
                               'form':form,
                               })
         
        
