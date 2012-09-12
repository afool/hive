from admins.models import ActivitiesInformation, Trend, CustomizeInformation
from accounts.models import UserProfile

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

from datetime import time, timedelta
import datetime

def get_last_activities():
    #under code is too long, must be refact code
    test_data = [ActivitiesInformation.objects.get_or_create(date=(datetime.date.today() - timedelta(days=2)).isoformat()),
                 ActivitiesInformation.objects.get_or_create(date=(datetime.date.today() - timedelta(days=1)).isoformat()),
                 ActivitiesInformation.objects.get_or_create(date=datetime.date.today().isoformat())]
    print test_data
    return test_data

def main(request):
    return render_to_response('admins/admins_main.html',RequestContext(request,{'last_activites':get_last_activities()}))


def activities_detail(request, year, month, day):
    date_stamp = datetime.datetime.strptime(year+month+day, "%Y%b%d")
    
    activities = ActivitiesInformation.objects.get(date__year=date_stamp.year,
                                                   date__month=date_stamp.month,
                                                   date__day=date_stamp.day)
    
    return render_to_response('admins/activities_detail.html',RequestContext(request,
                              {
                                'activities':activities
                                }))


def activities_form_set(request):
    pass


def activities_overview(request):
    try:
        activities_list = ActivitiesInformation.objects.all().order_by('-date')[:10]
    except ActivitiesInformation.DoesNotExist :
        print "Error, No ActivitiesInformation"
        raise Http404
    
    return render_to_response('admins/activities_overview.html',RequestContext(request,{
                                'activities_list':activities_list,
                               }))

def customize_detail(request, customize_id):
    pass


def trend_detail(request, year, month, day):
    date_stamp = datetime.datetime.strptime(year+month+day, "%Y%b%d")
    
    trend = get_object_or_404(Trend,
                              date__year=date_stamp.year,
                              date__month=date_stamp.month,
                              date__day=date_stamp.day)
    
    return render_to_response('admins/trend_detail.html',RequestContext(request,{
                               'trend':trend
                               }))
    
    
def trend_overview(request):
    try:
        trend_list = Trend.objects.all().order_by('-date')[:10]
    except Trend.DoesNotExist:
        print "Error, No Trend"
        raise Http404
    
    return render_to_response('admins/trend_overview.html',RequestContext(request,{
                                                                         'trend_list':trend_list
                                                                        }))
def analytics_detail(request, category):
    return render_to_response('admins/admins_'+category+'.html',RequestContext(request,{'latest_activities':get_last_activities()}))

def control_user(request):
    PAGE_SIZE = 20
    ban_id_list  = User.objects.all().exclude(is_active=True).exclude(username=request.user.username)
    staff_id_list = User.objects.all().exclude(is_staff=True).exclude(username=request.user.username)

    search_var = request.GET.get('search_var', None)
    url_search_param=""
    if search_var is None:
        people_profile_list=UserProfile.objects.select_related(depth=1).all().exclude(user=request.user)
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
    return render_to_response('admins/admins_user.html',RequestContext(request,
                                          {
                                            'is_menu_home':True,
                                            'is_peoplelist_active' : True,
                                            'ban_id_list':ban_id_list,
                                            'staff_id_list':staff_id_list,
                                            'peoples':peoples,
                                            'observer':observer,
                                            'url_search_param':url_search_param, }))

def ban_and_staff(request, category, method):
    def _staff_category():
        try:
            user = User.objects.get(id=user_id)
            if method == 'addstaff':
                user.is_staff = True
                user.is_superuser = True
            elif method == 'removestaff':
                user.is_staff = False
                user.is_superuser = False
            user.save()
            return True
        except:
            return False
    
    def _ban_category():
        try:
            user = User.objects.get(id=user_id)
            if method == 'addban':
                user.is_active = False
            elif method == 'removeban':
                user.is_active = True
            user.save()
            return True
        except:
            return False

    if request.GET.has_key('id'):
        user_id = request.GET['id']
        if category == 'staff':
            return HttpResponse(_staff_category())
        elif category == 'ban':
            return HttpResponse(_ban_category())
        else:
            return HttpResponse('Fail')
    else:
        return HttpResponse('Fail')

