from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/index.html', {'title':'Стартовая страница', 'tasks':tasks})

def pictures(request):
    return render(request,'main/pictures.html')

def about(request):
    return render(request,'main/about.html')

def create(request):
    error = ''
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена некорректно'
    form = TaskForm()
    context = {
        "form":form,
        "error":error
    }
    return render(request,'main/create.html',context)

def education(request):
    return render(request,'main/education.html',{'technology':'PYTHON','title':'Обучение программированию'})