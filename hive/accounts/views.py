from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from accounts.models import UserProfile, Following
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.validators import validate_email
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import UserRegistrationForm

from models import EmailActivation
import md5, time, datetime
from hive import settings 
# from django.core.cache import cache
# from accounts.models import *

def email_register_page(request):
    LETTER = '''Hello,\
        \nWelcome to HIVE!!\
        \nYou have to go %s%s for the activation.\
        \nGood Luck!\n\n- Hive, A fool team-'''
    def _keygen(email):
        email_key = md5.md5()
        email_key.update(email + str(time.time()))
        return email_key.hexdigest()

    def _is_registered(email):
        # Before registering user, we have to check both -
        # EmailActivation and User in sequence
        flag = True
        try:
            EmailActivation.objects.get(email=email)
        except ObjectDoesNotExist:
            flag = False
        
        if flag: return False
        
        try:
            User.objects.get(email=email)
            return False
        except ObjectDoesNotExist:
            return True
        

    def _is_validated(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
    
    if request.method == 'POST':
        try:
            email = request.POST['email']
                        
            if email and _is_registered(email) and _is_validated(email):
                to_email = [email, ]

                keygen = _keygen(email)
                expire_date = str(datetime.datetime.today()+datetime.timedelta(days=15))
                
                message = LETTER % ( settings.TEST_DOMAIN_NAME + 'accounts/activate_email/', keygen)
                
                send_mail('Hive Registration', message, 'astin@iz4u.net', to_email, fail_silently=False)
                                
                EmailActivation.objects.create(email=email, expire_date=expire_date, activation_key=keygen)
            else:
                status = 'Correct your email or already registered.'
                return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
        except BadHeaderError:
            status = 'Invalid access.'
            return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
    else:
        status = 'Invalid access.'
        return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))

    return HttpResponseRedirect('/')
    

def activation_page(request, key):
    try:
        user = EmailActivation.objects.get(activation_key=key)
    except ObjectDoesNotExist:
        status = 'Invalid access'
        return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
    if user and user.expire_date.date() >= datetime.datetime.today().date():
        form = UserRegistrationForm()
        return render_to_response('accounts/user_registration.html',
                                   RequestContext(request, {
                                    'form': form,
                                    'key': key,
                                    },))
    else:
        status = 'Invalid access'
        return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
# 340a1de9a00b30b5003f7057f167bf61
def register_userinfo_page(request, key):
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    else:
        userinfo_form = UserRegistrationForm(request.POST)
        
        if userinfo_form.is_valid():
            try:
                user = EmailActivation.objects.get(activation_key=key)
                
                userinfo_form.clean_username()
                userinfo_form.clean_password2()
                new_user = userinfo_form.save()
                
                new_user.email = user.email
                new_user.save() # Enroll Email
                user.delete() # Delete Activation Key
                
                UserProfile.objects.create(user=new_user)
                Following.objects.create(followee=new_user,
                                         followee_str = new_user.username,
                                         follower=new_user,
                                         follower_str = new_user.username)
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/')    
                        
        return HttpResponseRedirect('/')            

def forgot_password_page(request):
    LETTER = '''Hello,\
        \nYou've forgot the password!!\
        \nYou have to go %s%s for the renew.\
        \nGood Luck!\n\n- Hive, A fool team-'''
    def _keygen(email):
        email_key = md5.md5()
        email_key.update(email + str(time.time()))
        return email_key.hexdigest()

    def _is_registered(email):
        try:
            User.objects.get(email=email)
            return True
        except ObjectDoesNotExist:
            return False
        
    def _is_validated(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
        
    if request.method == 'POST':
        try:
            email = request.POST['email']
                        
            if email and _is_registered(email) and _is_validated(email):
                to_email = [email, ]

                keygen = _keygen(email)
                expire_date = str(datetime.datetime.today()+datetime.timedelta(days=15))
                
                message = LETTER % ( settings.TEST_DOMAIN_NAME + 'accounts/renew_password_email/', keygen)
                
                send_mail('Hive Password Renew', message, 'astin@iz4u.net', to_email, fail_silently=False)
                                
                EmailActivation.objects.create(email=email, expire_date=expire_date, activation_key=keygen)
            else:
                status = 'Correct your email or No user.'
                return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
        except BadHeaderError:
            status = 'Invalid access.'
            return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))
    else:
        status = 'Invalid access.'
        return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))

    return HttpResponseRedirect('/')

def renew_password_email_page(request, key):
    try:
        user_act = EmailActivation.objects.get(activation_key=key)
        user = User.objects.get(email=user_act.email)
        form = SetPasswordForm(forms.Form)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    
    return render_to_response('accounts/renew_password.html',
                                       RequestContext(request,
                                                      {'form': form,
                                                       'key': key}))

def renew_password_page(request, key):
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    else:
        user_act = EmailActivation.objects.get(activation_key=key)
        user = User.objects.get(email=user_act.email) 
        user_form = SetPasswordForm(request.POST)
        if user_form.is_valid():
            user_form.clean_new_password2()
            user_form.save()
            try:
                user_act = EmailActivation.objects.get(activation_key=key)
                user_act.delete() # Delete Activation Key
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/')    
                        
        return HttpResponseRedirect('/')
    
def profile_page(request, username):
    user = None
    if username is None:
        user = request.user
    else :
        user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user = user)
    return render_to_response('accounts/detail_profile.html', RequestContext(request,{
                                                               'user' : user,
                                                               'user_profile':user_profile,
                                                               }))

def people_list_page(request):
    PAGE_SIZE = 20
    
    followers_id_list = Following.objects.filter(
         follower =request.user ).values_list('followee',flat=True)
    search_var = request.GET.get('search_var', None)
    url_search_param=""
    if search_var is None:
        people_profile_list=UserProfile.objects.select_related(depth=1).all()
    else :
        url_search_param="&search_var=%s" %(search_var)
        people_profile_list = UserProfile.objects.select_related().all().filter(user__in=User.objects.all().filter(username__icontains=search_var))
    
    paginator = Paginator(people_profile_list, PAGE_SIZE)
    page = request.GET.get('page',1)
    try:
        peoples = paginator.page(page)
    except PageNotAnInteger:
        peoples = paginator.page(1)
    except EmptyPage:
        peoples = paginator.page(paginator.num_pages)

    observer = request.user
    return render_to_response('accounts/people_list_page.html',RequestContext(request,
                                          {
                                            'followers_id_list':followers_id_list,
                                           'peoples':peoples,
                                           'observer':observer,
                                           'url_search_param':url_search_param, }))

def add_follow_page(request, followee_id):
    followee = User.objects.get(id=followee_id )
    if not Following.objects.filter(followee=followee, follower =request.user ).count():
        Following.objects.create(followee=followee, follower =request.user )
    return HttpResponse("OK")

def remove_follow_page(request, followee_id):
    followee = User.objects.get(id=followee_id )
    Following.objects.filter(followee=followee, follower =request.user ).all().delete()
    return HttpResponse("OK")
