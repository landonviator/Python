from django.shortcuts import render
from django.http import HttpResponse

def myView(requests):
    return HttpResponse('Hello')