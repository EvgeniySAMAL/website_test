from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/index.html', {'title':'Стартовая страница', 'tasks':tasks})

def pictures(request):
    return render(request,'main/pictures.html')

def about(request):
    return render(request,'main/about.html')

def create(request):
    return render(request,'main/create.html')

def education(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/education.html', {'technology':'PYTHON', 'tasks':tasks})