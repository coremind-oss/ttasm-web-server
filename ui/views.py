import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    
#     print(request.user)
#     print(type(request.user))
#     print(dir(request.user))
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

def showing_reverse(request):
    logout(request)
    messages.warning(request, 'You have been logged out due to inactivity')
    return redirect('/')

@csrf_exempt
def desktop_router(request):
    print(request.POST)
    body_json = bytes.decode(request.body)
    parsedJSON = json.JSONDecoder().decode(body_json)
    print(type(parsedJSON), parsedJSON)
    some_dict = {
        'server': 'this is a server message',
    }
    data = json.JSONEncoder().encode(some_dict)
    return HttpResponse(data)

def public_key(request, pub_key_hash=None):
    if settings.ID_RSA_PUB_HASH == pub_key_hash:
        return HttpResponse('Public key up to date')
    return HttpResponse(settings.ID_RSA.publickey().exportKey())

@csrf_exempt
def client_key_hash(request, client_key_hash=None):

    print(request.POST['hash'])
#     print(User.objects.all())#
#     print(User.get_user(request))
    current_user = request.user
    print (current_user)

    #print(User.objects.get(User.username = 'luka')

    #check if client's hash matches the one in DB
    return HttpResponse(request.POST)
    pass

@csrf_exempt
def client_key(request, client_key=None):

    print(request.POST['user'])
    print(request.POST['pub_key'])

    return HttpResponse('client key received')
    pass

