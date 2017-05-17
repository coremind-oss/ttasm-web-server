from django.contrib import messages
from django.contrib.auth.views import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


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
