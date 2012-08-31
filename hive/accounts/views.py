from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.validators import validate_email
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
        try:
            EmailActivation.objects.get(email=email)
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
                        
            if _is_registered(email) and _is_validated(email):
                to_email = [email, ]

                keygen = _keygen(email)
                expire_date = str(datetime.datetime.today()+datetime.timedelta(days=15))
                
                # Temp to write http~~ TODO: should change variable.
                message = LETTER % ( settings.TEST_DOMAIN_NAME + 'accounts/activate_email/', keygen)
                print message
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
    user = EmailActivation.objects.get(activation_key=key)
    if user and user.expire_date.date() >= datetime.datetime.today().date():
        form = UserRegistrationForm()
        return render_to_response('accounts/user_registration.html',
                                   RequestContext(request, {
                                    'form': form,
                                    },))
    else:
        status = 'Invalid access'
        return render_to_response('accounts/login.html',
                                           RequestContext(request,
                                                          {'form': AuthenticationForm(),
                                                           'status': status}))


def register_userinfo_page(request):
    if request.method != "POST" :
        return HttpResponseRedirect('/')
    else:
        userinfo_form = UserRegistrationForm(request.POST)
        
        if userinfo_form.is_valid():
            try:
                userinfo_form.clean_username()
                userinfo_form.clean_password2()
                userinfo_form.save()
            except userinfo_form.ValidationError:
                return HttpResponseRedirect('/')    
                        
        return HttpResponseRedirect('/')            

def renew_password_page(request, key):
    pass

def reset_password_page(request):
    form = PasswordChangeForm(SetPasswordForm(forms.Form))
    return render_to_response('accounts/reset_password.html',
                                           RequestContext(request,
                                                          {'form': form}))

def userinfo_page(request):
    return HttpResponse(request.user)

def followlist_page(request):
    pass

def addfollow_page(request):
    pass

def finduser_page(request):
    pass

