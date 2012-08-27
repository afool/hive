# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from smtplib import SMTPException


# from django.core.cache import cache
# from accounts.models import *

def main_page(request):
    return HttpResponseRedirect('index.html')

def register_page(request):
    if request.method == 'POST':
        # TODO: Check email type here or using Javascript

        try:
            to_email = request.POST['signup_email']
            # TODO: check duplicated e-mail

            # TODO: Generates confirmed random key
            gen_key = 'temporary'

            send_mail('Hive Registration', gen_key, 'entertainer7@dreamwiz.com', to_email, fail_silently=False)
            print "1234"
        except BadHeaderError:
            return HttpResponseRedirect('Invalid header found.')
        except SMTPException:
            print "aaaa"
        except: # what exception object?
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


