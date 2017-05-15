from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is the index page')

def catch_all(request):
    return redirect('index')