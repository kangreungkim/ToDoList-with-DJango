from typing import Any
from django.shortcuts import render
#from http.client import HTTPResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HTTPResponse('my_to_do_app first page')
    return HttpResponse('my_to_do_app first page')