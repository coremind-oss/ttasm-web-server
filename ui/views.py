from _datetime import timezone, datetime
import json, base64, uuid
import traceback

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import pytz

from allauth.account.decorators import verified_email_required
from data.models import DailyActivity
from data.models import Desktop
from ttasm_web_server.slack import send_exception
from django.http.request import HttpRequest


@verified_email_required
def index(request):
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

@verified_email_required
def profile(request):
    print('JUST GOT ACCESSED BY:', request.user)
    return render(request, template_name='ui/user/profile.html')

def showing_reverse(request):
    logout(request)
    messages.warning(request, 'You have been logged out due to inactivity')
    return redirect('/')

@ensure_csrf_cookie
def public_key(request):
    return HttpResponse(settings.ID_RSA.publickey().exportKey())

@csrf_exempt
def desktop_login(request):
    #Uses django's authenticate function to compare user/pws with db data.
    try:
        post = request.POST
        if request.method == 'POST' and\
        'username' in post and\
        'password' in post and\
        'client_public_key' in post and\
        'uuid' in post:
            username = post['username']
            password = post['password']
            client_public_key = post['client_public_key']
            uuid = post['uuid']
            print ('User {} is trying to log in'.format(username))

            user_obj = authenticate(username = username, password = password)

            if user_obj is not None:
                token = get_random_string(40)
                desktop_obj, created = Desktop.objects.get_or_create(
                    name = username,
                    defaults = {
                        'name': username,
                        'public_key': client_public_key,
                        'uuid' : uuid,
                        'token' : token
                    }
                )
                if not created:
                    desktop_obj.public_key = client_public_key
                    desktop_obj.uuid = uuid
                    desktop_obj.token = token
                    desktop_obj.save()
                #desktop_obj.socket_token = token
                return JsonResponse({ 'status': 'ok', 'token': token })

            else:
                return HttpResponse('Invalid user/pass, access denied')
        else:
            return HttpResponse('Invalid access method. Only POST allowed.')
    except:
        send_exception(traceback.format_exc(), '#exceptions')
        
        
def get_last_timestamp(request):
    

    daily_activity = DailyActivity.objects.filter(user=request.user)
    last_daily_activity = daily_activity.last()
    last_daily_activity_timestamp = last_daily_activity.data[0]['timestamp']
#     return last_daily_activity_timestamp
    return HttpResponse(last_daily_activity_timestamp)

def timestamp_message_handling(request):
    
    try:
        print(request.user)
        post = request.POST
        
        if request.method == 'POST' and 'message' in post and 'base_date' in post:
            message = post['message']
# <<<<<<< HEAD
#             timestamp = post['timestamp']
#             json_data = {'message':message, 'timestamp':timestamp}
# 
#             u = User.objects.filter(username='danijel').get()
# 
#             daily_a_obj = DailyActivity.objects.create(user = u)
#             daily_a_obj.data.append(json_data)
#             daily_a_obj.save()
# =======

            base_date = post['base_date']
            timestamp = timezone.now(pytz.utc)
            json_data = { 'message': message, 'timestamp': timestamp }

            daily_activity, created = DailyActivity.objects.get_or_create(
                base_date=base_date,
                user=request.user,
                defaults={
                    'base_date': base_date,
                    'user': request.user,
                    'data': json_data,
                }
            )
            
            if not created:
                daily_activity.data.append(json_data)
                daily_activity.save()
# >>>>>>> 42b24f056362a7a72839b863f29a0a6a018ece52

#             return HttpResponse("This was sent:{}  {}  {} ".format(timestamp,message))
            return HttpResponse('The message was saved in database')
        else:
            return HttpResponse('Cannot write into database')
    except:
        print("Server didnt't receive any message")
        print(traceback.format_exc())
        return HttpResponse()