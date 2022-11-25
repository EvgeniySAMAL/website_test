from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request,'main/index.html', {'title':'Стартовая страница', 'tasks':tasks})

def pictures(request):
    return render(request,'main/pictures.html')

def about(request):
    return render(request,'main/about.html')