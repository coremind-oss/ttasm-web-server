

import json

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.handlers.modwsgi import groups_for_user
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import data


# Create your views here.
def index(request):
#     return HttpResponse("this is shortys index page")
 
 
#     groups = request.user.groups.all()
#     print(request.user.groups.all())
#      
#     for group in groups:
#         print(group)
     
     
 
 
    print(request.user)
    print(dir(request.user))
        
    for item in dir(request.user):
        print('request.user.{}'.format(item))
 
    context_index = {'name': 'Danijel',
                     'data':{'example':'example of data'},
                         'some_list':[
                             'item1',
                             'item2',
                             'item3',
                             'item4',
                             'item5',
                             'item6',
                             'item7',                      
                         ]
                      
                    }
    return render(request, template_name = 'index.html', context=context_index)

def reverse_link(request):
    return HttpResponse('This is reverse link built through django')

def inactivity(request):
    return HttpResponse('this is inactivity')

def logout_page(request):
    logout(request)
    messages.warning(request, 'Your session has expired')
    return render(request, template_name = 'logout_page.html')

@csrf_exempt
def desktop_router(request):
    print(request.POST)
    dict = {'ime servera':'server 1'}
    data = json.JSONEncoder().encode(dict)
    return HttpResponse(data)


  

    