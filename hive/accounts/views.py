# Create your views here.
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
    def _email_key_gen(email):
        email_key = md5.md5()
        email_key.update(email + str(time.time()))
        return email_key.hexdigest()

    def _already_registerd_email(email):
        try:
            EmailActivation.objects.get(email_address=eamil)
            return False
        except:
            return True

    def _check_email(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    if request.method == 'POST':
        post_email = request.POST['signup_email']
        try:
            if _already_registerd_email is True and _check_email(post_email) is True:
                to_email = []
                to_email.append(post_email)

                gen_key = email_key_gen(post_email)
                expire_date = str(datetime.datetime.today()+datetime.timedelta(days=15))

                send_mail('Hive Registration', gen_key, 'astin@iz4u.net', to_email, fail_silently=False)
                EmailActivation.objects.create(email_address=post_email, expire_date=expire_date, activation_key=gen_key)
            else:
                HttpResponse("Your mail is already enrolled.")
        except BadHeaderError:
            return HttpResponseRedirect('Invalid header found.')
        except SMTPException:
            pass
    else:
        pass # raise invaild method.

    return HttpResponseRedirect('../../')


def userinfo_page(request):
    pass

def settings_page(request):
    pass

def followlist_page(request):
    pass

def finduser_page(request):
    pass

def logout_page(request):
    pass


