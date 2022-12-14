from .models import Task
from django.forms import ModelForm, TextInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task","technology"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "technology": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
        }