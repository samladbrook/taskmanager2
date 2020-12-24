from django.shortcuts import render
from .models import Tasks
from django.http import HttpResponse, request

# Create your views here.

def home(request):
    return render(request, 'home.html')

def main(request):

    tasks = Tasks.objects
    tasknum = 0
    return render(request, 'main.html', { 'tasks':tasks })





#    tasks = Task.objects.all()
#, {'tasks' : tasks})