from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html')

def pictures(request):
    return render(request,'main/pictures.html')

def about(request):
    return render(request,'main/about.html')