from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return HttpResponse("Hello,world!")


def register(request):
    return HttpResponse("This is the registration page")
