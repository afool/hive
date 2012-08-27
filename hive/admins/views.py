from django.shortcuts import render_to_response, get_object_or_404
from admins.models import ActivitiesInformation, Trend, CustomizeInformation 
import datetime, time

def index(request):
    latest_activities = list(ActivitiesInformation.objects.all().order_by('-date')[:1]).pop()
    trend_list = Trend.objects.all().order_by('date')[:20]
    
    
    return render_to_response('admins/admins_index.html',
                              {
                                'latest_activities':latest_activities,
                                'trend_list':trend_list
                               }
                              )

def activities_overview(request):
    activities_list = ActivitiesInformation.objects.all().order_by('-date')[:10]
    
    return render_to_response('admins/activities_overview.html',
                              {
                                'activities_list':activities_list,
                               })

def activities_detail(request, year, month, day):
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    
    activities = ActivitiesInformation.objects.get(date__year=pub_date.year,
                                                   date__month=pub_date.month,
                                                   date__day=pub_date.day)
    
    return render_to_response('admins/activities_detail.html',
                              {
                                'activities':activities
                                })

def trend_overview(request):
    trend_list = Trend.objects.all().order_by('-date')[:10]
    return render_to_response('admins/trend_overview.html',
                              {
                                'trend_list':trend_list
                               })

def trend_detail(request, year, month, day):
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    
    trend = get_object_or_404(Trend,
                              date__year=pub_date.year,
                              date__month=pub_date.month,
                              date__day=pub_date.day)
    
    return render_to_response('admins/trend_detail.html',
                              { 
                               'trend':trend
                               })

def customize_detail(request, customize_id):
    pass
