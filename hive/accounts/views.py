from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from accounts.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.validators import validate_email
from forms import EmailRegistrationForm
from smtplib import SMTPException
from django.core.exceptions import ValidationError

import md5, time, datetime

# from django.core.cache import cache
# from accounts.models import *

def login_page(request):
    reg_form = EmailRegistrationForm()
    return render_to_response('/accounts/login.html',
                            RequestContext(request, {
                                'reg_form': reg_form
                            } ))

def email_register_page(request):
    LETTER = '''Hello,\
        \nWelcome to HIVE!!\
        \nYou have to go %s/%s for the activation.\
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
                message = LETTER % ('http://localhost:8000/accounts/?activation_key=', keygen)
                send_mail('Hive Registration', message, 'astin@iz4u.net', to_email, fail_silently=False)
                                
                EmailActivation.objects.create(email=email, expire_date=expire_date, activation_key=keygen)
            else:
                HttpResponse("Your mail is already enrolled.")
        except BadHeaderError:
            return HttpResponseRedirect('Invalid header found.')
        except SMTPException:
            pass
    else:
        return HttpResponseRedirect('Invalid access method.')

    return HttpResponseRedirect('../../')
    

def confirmed_activation_page(request):
    pass

def userinfo_page(request):
    return HttpResponse(request.user)

def followlist_page(request):
    pass

def addfollow_page(request):
    pass

def finduser_page(request):
    pass

def logout_page(request):
    pass
