import json

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


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


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, template_name='ui/register.html')

    elif request.method == 'POST':
        form_data = request.POST

        # Check if username exists
        if User.objects.filter(username=form_data['username']).exists():
            messages.warning(request, 'Username {} allready exists'.format(form_data['username']))
            return(redirect('register'))
        else:
            username = form_data['username']
            raw_password = form_data['password1']
            first_name = form_data['first_name']
            last_name = form_data['last_name']
            email = form_data['email']

            # Create user with all fields and store it in database
            user = User.objects.create_user(username, email, raw_password)
            user.is_active = False
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return(redirect('index'))


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
