from forms import PostForm, AttachmentForm
from posts.models import Post, Like, Comment, Attachment
from timelines.models import Timeline

from django.contrib.auth.decorators import login_required
from django.db.models import F

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json


@login_required(login_url='/accounts/login')
def create_comment(request, post_id):
    if request.method != "POST" :
        print "Error, Invalid access. <%s>" %(request.method)
        return HttpResponseRedirect('/')
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist :
        print "Can't find Post <id:%d>" %(post_id)
        return HttpResponseRedirect('/')
    
    comment_text = request.POST['comment_text']
    post.comments_count = F('comments_count')+1
    post.save()
    Comment.objects.create(text=comment_text,
                                         writer=request.user,
                                         author=request.user.username,
                                         post=post)
    if request.is_ajax():
        post = Post.objects.get(id=post_id)
        comment_list = post.comment_set.all()
        return render_to_response('posts/post_render.html',
                    RequestContext(request,
                     {"post":post,
                      "comment_list" : comment_list }))
    return HttpResponseRedirect('/#post_' + post_id)


@login_required(login_url='/accounts/login')
def create_post_timeline(request):
    if request.method != "POST" :
        HttpResponseRedirect('/')
        
    if request.user.is_authenticated() is False:
            return HttpResponseRedirect('/accounts/login')
        
    post_contents = request.POST['post_contents']
    post = Post.objects.create(contents=post_contents, writer=request.user, author=request.user.username)
    post.save()
    
    # fix uploaded data
    if request.session.has_key("temporary_post_id"):
        if request.session.has_key("upload_images"):
            p = Post.objects.get(id=1)
            upload_images = request.session["upload_images"]
            Attachment.objects.filter(post=p).filter( 
                id__in = upload_images ).update(post = post)
            del request.session["upload_images"]            
        del request.session["temporary_post_id"]
    
    Timeline.objects.create(post = post, writer=post.writer)
    return HttpResponseRedirect('/')


def index(request):
    pass


@login_required(login_url='/accounts/login')
def on_liked(request, post_id):
    try :
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        raise Http404
    
    like = Like.objects.create(liker=request.user, post=post)
    like.save()
    post.on_liked(request.user)
    
    # To Do : just re render only the Liked Post ( not redirect and render whole page)
    return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login')
def on_unliked(request, post_id):
    try:
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        print "Can't find Post id:%d" %(post_id)
        raise Http404
    
    try:
        like = Like.objects.get(post=post, liker=request.user)
    except Like.DoesNotExist:
        print "Can't find Like about %s by %s" %(post, request.user)
        raise Http404
    
    post.on_unliked(like.liker)
    like.delete()
    
    # To Do : just re render only the Liked Post ( not redirect and render whole page)
    return HttpResponseRedirect('/')


def one_of_post_detail(request, post_id):
    try:
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        raise Http404
    if request.is_ajax():
        return render_to_response('posts/post_render.html',
                    RequestContext(request, {"post":post}))
    return render_to_response('posts/post_detail.html', RequestContext(request, {
                             'post': post
                            }))    


@login_required(login_url='/accounts/login')
def recent_photos(request):
    
    images = [
        {"thumb": obj.upload.url, "image": obj.upload.url}
        for obj in Attachment.objects.filter(is_image=True).order_by("-create_time")[:20]
    ]
    return HttpResponse(json.dumps(images), mimetype="application/json")


@login_required(login_url='/accounts/login')
def upload_attachments(request):
    if request.method == "POST":
        attachment_form = AttachmentForm(request.POST, request.FILES)
        print request.POST, request.FILES
        if attachment_form.is_valid():
            attachment_form.save()
            return HttpResponseRedirect('/')
    else:
        form = AttachmentForm()
        return render_to_response('posts/upload_attachments.html', RequestContext(request, {'form':form}))


@csrf_exempt
@require_POST
@login_required(login_url='/accounts/login')
def upload_photos(request):
    if request.session.has_key("upload_images"):
        del request.session["upload_images"]
    if not request.session.has_key("upload_images"):
        request.session["upload_images"] = []
        upload_images = []
    
    if request.session.has_key("temporary_post_id"):
        del request.session["temporary_post_id"] 
    if not request.session.has_key("temporary_post_id"):
        request.session["temporary_post_id"] = 1
    # TODO fix temporary post id    
   
    images = []
    post = Post.objects.get(id=1)
    for f in request.FILES.getlist("file"):
        obj = Attachment.objects.create(post = post , upload=f, is_image=True)
        images.append({"filelink": obj.upload.url})
        upload_images.append(obj.id)
        print obj.id
    request.session["upload_images"] = upload_images
    print request.session["upload_images"]
    request.session.modified = True
    return HttpResponse(json.dumps(images), mimetype="application/json")

