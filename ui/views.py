from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):

#     print(request.user)
#     print(type(request.user))
#     print(dir(request.user))

    groups = request.user.groups.all()
    print(groups)
    groups = groups.filter(name__contains='i')
    print(groups)
    groups = groups.filter(name='sales')
    print(groups)
    for group in groups:
        print(group)

#     for item in dir(request.user):
#         print('request.user.{}'.format(item))

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
    return HttpResponse('reverse example')
