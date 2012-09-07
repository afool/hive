from admins.models import ActivitiesInformation, Trend, CustomizeInformation

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
 
import datetime, time

def index(request):
    try:
        latest_activities = ActivitiesInformation.objects.all().order_by('-date')[:1].get()        
#        
#        activities_list = list(ActivitiesInformation.objects.all().order_by('-date')[:1])
#        if len(activities_list) is 0:
#            print "Error, No Activities Information"
#            raise Http404
    except ActivitiesInformation.DoesNotExist:
        raise Http404
    
    trend_list = Trend.objects.all().order_by('date')[:20]
    
    return render_to_response('admins/admins_index.html',RequestContext(request,{
                                'latest_activities':latest_activities,
                                'trend_list':trend_list
                               }))


def activities_detail(request, year, month, day):
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    
    activities = ActivitiesInformation.objects.get(date__year=pub_date.year,
                                                   date__month=pub_date.month,
                                                   date__day=pub_date.day)
    
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
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    
    trend = get_object_or_404(Trend,
                              date__year=pub_date.year,
                              date__month=pub_date.month,
                              date__day=pub_date.day)
    
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

def test_page(request):
    test_data = {'x':{'a', 'b', 'c', 'd', 'e', 'f'}, 
                 'y':{1, 2, 3, 4, 10, 1, 30}}
    return render_to_response('admins/test.html',{'datas':test_data})
