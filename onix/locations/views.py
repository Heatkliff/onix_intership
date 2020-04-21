from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is locations index.")


def static_link(request):
    return HttpResponse("Hello, this is static page.")


def dynamic(request, variable):
    return HttpResponse(f"Hello, variable - {variable}.")


def media_picture(request):
    return HttpResponse(f"<img src='/media/django.jpg'>")


def bootstrap_link(request):
    return HttpResponse(f"<a href='/static/css/bootstrap.css'>CSS Bootstrap</>")
