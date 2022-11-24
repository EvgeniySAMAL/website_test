from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Hello</h4>")

def pictures(request):
    return HttpResponse("<h1>this page is for pictures</h1>")