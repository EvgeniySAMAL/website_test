from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def pictures(request):
    return HttpResponse("<h1>this page is for pictures</h1>")

def about(request):
    return HttpResponse("<h1>about</h1>")