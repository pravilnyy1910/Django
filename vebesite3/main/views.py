from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(reguest):
    task = Task.objects.all()
    return render(reguest, 'main/index.html', {'title': 'Главная страница', 'tasks': 'title'})

def about(regust):
    return render(regust, 'main/about.html')
