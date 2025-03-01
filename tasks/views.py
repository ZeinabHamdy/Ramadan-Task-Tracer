from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import AddTaskForm
from django import forms

# Create your views here.

@login_required
def tasks_view(req):
    '''
        get all tasks for the current user in that day
    '''
    today = datetime.today().date()  
    tasks = Task.objects.filter(user=req.user, created_at__date=today)
    context = {
        'tasks': tasks,
    }
    return render(req, 'tasks.html', context)


@login_required
def task_details(req, task_id):
    task = get_object_or_404(Task, id=task_id, user=req.user)
    context = {
        'task': task,
        'title': task.title,
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