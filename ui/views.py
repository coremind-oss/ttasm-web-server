import json, base64

from django.conf import settings
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.contrib.auth.views import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from utility import decrypt_data
from data.models import Client_Key



@verified_email_required
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

def profile(request):
    return render(request, template_name='ui/user/profile.html')

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
def client_key(request):

    try:
        request.POST['user']
        request.POST['pub_key']
    except:
        error_message = 'Client key not posted with request.'
        print (error_message)
        return HttpResponse(error_message)
    
    
    try:
        client_key_DB = Client_Key.objects.get(pub_key=request.POST['pub_key'])
        print ('Client key found on server')
        return HttpResponse('Client key already on server')
    except Exception as e:
        print (e, type(e))
        print ('Key not found, saving to database')
        try:
            #user = User.objects.get(username=request.POST['user'])
            u = User.objects.get(username=request.POST['user'])
            c = Client_Key(pub_key = request.POST['pub_key'], user = u)
            #print (c, c.user)
            c.save()
            print('Saved client key to database')

        except Exception as e:
            print ('except: ', e)
            print ('User not found') 


    return HttpResponse('client key')

@csrf_exempt
def auth(request):
    #Calls django's authenticate function to compare user/pws with db data. Posted data must first be decrypted

    print ('Got authentication request from {}'.format(request.get_host()))
    
    try:
        user = request.POST['user']
        base64_data = request.POST['enc_data']
    
    except:
        message = 'No authentification data posted' 
        print (message)
        return HttpResponse(message)    
    
    enc_data = base64.b64decode(base64_data)
    user_obj = User.objects.get(username=user)
    print (user_obj)

    print ('Len of enc_data on server:', len(enc_data))
    
    decrypted_data = decrypt_data(enc_data, settings.ID_RSA.exportKey())
    print ('Decrypt data result:', decrypted_data)
    dict = json.loads(decrypted_data.decode()) 

    try:
        user_obj = authenticate(username = user, password = dict['pass'])
    except Exception as e:
        print ('except:', e)
        
    if user_obj is not None:
        print('User {} logged in'.format(user))
        #start_socket_connection(user)
        #start_session(user)?
        return HttpResponse('ok')
    else:
        message = 'Invalid user/pass, access denied'
        print(message)
        return HttpResponse(message)
            



