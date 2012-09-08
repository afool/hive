from admins.models import ActivitiesInformation, Trend, CustomizeInformation

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import datetime
from datetime import time, timedelta

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
