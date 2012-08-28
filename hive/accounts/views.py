from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.validators import validate_email
from smtplib import SMTPException
from accounts.models import *
import md5, time, datetime

# from django.core.cache import cache
# from accounts.models import *

def email_register_page(request):
    def _keygen(email):
        email_key = md5.md5()
        email_key.update(email + str(time.time()))
        return email_key.hexdigest()

    def _is_registered(email):
        try:
            EmailActivation.objects.get(email_address=eamil)
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
        post_email = request.POST['signup_email']
        try:
            if _is_registered and _is_validated(post_email):
                to_email = []
                to_email.append(post_email)

                keygen = _keygen(post_email)
                expire_date = str(datetime.datetime.today()+datetime.timedelta(days=15))

                # TODO: Send url for activation

                send_mail('Hive Registration', keygen, 'astin@iz4u.net', to_email, fail_silently=False)
                EmailActivation.objects.create(email_address=post_email, expire_date=expire_date, activation_key=keygen)
            else:
                HttpResponse("Your mail is already enrolled.")
        except BadHeaderError:
            return HttpResponseRedirect('Invalid header found.')
        except SMTPException:
            pass
    else:
        return HttpResponseRedirect('Invalid access method.')


    return HttpResponseRedirect('../../')

def login_page(request):
    if request.POST.has_key('login_email') and request.POST.has_key('password'):
        # try:
        email = request.POST['login_email']
        username = User.objects.get(email=email).username
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_authenticated:
                login(request, user)
                return HttpResponse('Success')
            elif user.is_active is False:
                pass # TODO: lead user to activate
            else:
                return HttpResponse('Login Fail')
        #except:
    else:
        pass

    return HttpResponse('...')

def userinfo_page(request):
    pass

def followlist_page(request):
    pass

def addfollow_page(request):
    pass

def finduser_page(request):
    pass

def logout_page(request):
    pass
