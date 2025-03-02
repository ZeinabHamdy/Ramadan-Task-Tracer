from .forms import AddTaskForm
from .models import Task

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.contrib import messages
from django.db.models import Avg
from datetime import datetime
from django import forms

# Create your views here.

@login_required
def tasks_view(req):
    user = req.user
    today = now().date()  
    tasks = Task.objects.filter(user=user, created_at__date=today)
    context = {
        'tasks': tasks,
    }
    return render(req, 'tasks.html', context)


@login_required
def task_details(req, task_id):
    task = get_object_or_404(Task, id=task_id, user=req.user)
    context = {
        'task': task,
    }
    return render(req, 'task_details.html', context)


@login_required
def add_task(req):
    user = req.user 
    if req.method == 'POST':
        form = AddTaskForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            messages.success(req, 'Task added successfully')
            return redirect('tasks')
    else:
        form = AddTaskForm()
    context = {
        'form': form,
        'task': 0,
    }
    return render(req, 'add_task.html', context)



@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('tasks')
    else:
        form = AddTaskForm(instance=task)
    context = {
        'form': form,
        'task': 1,
    }
    return render(request, 'add_task.html', context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('tasks')



from django.shortcuts import render
import random

def home(req):
    
    user = req.user
    today = now().date()  
    tasks_today = Task.objects.filter(user=user, created_at__date=today)

    avg_progress = tasks_today.aggregate(avg_progress=Avg('progress'))['avg_progress'] or 0
    
    
    context = {
        "progress": min(100.0,round(avg_progress, 2)),
        'signed': req.user.is_authenticated,
    }
    
    return render(req, "home.html", context)


def progress_overview(request):
    user = request.user
    task_dates = Task.objects.filter(user=user).dates('created_at', 'day')

    progress_by_day = []
    for date in task_dates:
        tasks_on_day = Task.objects.filter(user=user, created_at__date=date)
        avg_progress = tasks_on_day.aggregate(avg_progress=Avg('progress'))['avg_progress'] or 0

        progress_by_day.append({
            'date': date,
            'tasks': tasks_on_day,
            'avg_progress': round(avg_progress, 2),
        })

    context = {
        'progress_by_day': progress_by_day,
    }

    return render(request, 'progress_overview.html', context)