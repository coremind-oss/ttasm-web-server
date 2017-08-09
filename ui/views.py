from datetime import datetime
import traceback
import uuid

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from allauth.account.decorators import verified_email_required
from data.models import DailyActivity
from data.models import Desktop
from ttasm_web_server.slack import send_exception
from ttasm_web_server.utils import human_time
from utility import get_base_date


@verified_email_required
def index(request):
    print(request.COOKIES)
    print('ID:', request.user.id)

    for item in dir(request.user):
        print('request.user.{}'.format(item))

    context_built = {
        'data': 'I am data',
        'data1': 'I am data1',
        'some_dict': {
            'dict_data': 'I am dict data',
        },
        'some_list': [
            'item 1',
            'item 2',
            'item 3',
            'item 4',
        ]
    }

    kwargs = {
        'context': context_built,
        'content_type': None,
        'status': None,
        'using': None,
    }

    return render(request, template_name='ui/index.html', **kwargs)


def get_daily_activities(request):
    context = {
        'daily_activities' : DailyActivity.objects.filter(user=request.user)
    }

    return render(request, template_name='ui/user/d_activities.html', context=context)



@verified_email_required
def profile(request):
    print(request.COOKIES)
    print('JUST GOT ACCESSED BY:', request.user)
    return render(request, template_name='ui/user/profile.html')

@ensure_csrf_cookie
def public_key(request):
    return HttpResponse(settings.ID_RSA.publickey().exportKey())



@verified_email_required
def timestamp_message_handling(request):
    try:
        print(request.user)
        post = request.POST
        
        if request.method == 'POST' and 'message' in post and 'timezone' in post:
            message = post['message']
            base_date = get_base_date(post['timezone'])
            timestamp = timezone.now()
            json_data = { 
                'message': message,
                'timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%SZ%z')
            }

            daily_activity, created = DailyActivity.objects.get_or_create(
                base_date=base_date,
                user=request.user,
                defaults={
                    'base_date': base_date,
                    'user': request.user,
                    'data': [json_data],
                }
            )
            
            if not created:
                daily_activity.data.append(json_data)
                daily_activity.save()
            return HttpResponse('The message was saved in database')
        else:
            return HttpResponse('Cannot write into database')
    except:
        print("Server didnt't receive any message")
        print(traceback.format_exc())
        return HttpResponse()

@verified_email_required
def initial_synchronization(request):
    if request.method == 'GET':
        base_date = get_base_date(request.GET['timezone'])

        daily_activity = DailyActivity.objects.get_or_create(
            user=request.user,
            base_date=base_date,
            defaults={
                'base_date': base_date,
                'user': request.user,
                'data': [{ 
                    'message': 'Start of your working day.',
                    'timestamp': timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ%z')
                }]
            }
        )[0]
        
        last_daily_activity_timestamp = daily_activity.data[-1]['timestamp']
        
        return HttpResponse(last_daily_activity_timestamp)
    else:
        return HttpResponse('bad request')
    
@verified_email_required  
def last_activity_duration(request):
    current_time = timezone.now()
    daily_activity = DailyActivity.objects.filter(user=request.user).last()
    last_timestamp = daily_activity.data[-1]['timestamp']
    last_timestamp = datetime.strptime(last_timestamp, '%Y-%m-%dT%H:%M:%SZ%z')
    time_passed = human_time(current_time - last_timestamp)
    return HttpResponse(time_passed)

@verified_email_required  
def user_logout(request):
    user = request.user
    logout(request)
    return HttpResponse('User is logged out and user is: {}'.format(user))

def inactivity_logout(request):
    print(request.COOKIES)
    logout(request)
    messages.warning(request, 'You have been logged out due to inactivity')
    return redirect('/')
