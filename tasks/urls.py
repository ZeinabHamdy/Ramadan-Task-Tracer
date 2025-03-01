from django.urls import path, include
from .views import tasks_view, task_details, add_task

urlpatterns = [
    path('tasks/', tasks_view, name='tasks'),
    path('task/<int:task_id>/', task_details, name='task_details'),
    path('add_task/', add_task, name='add_task'),


]
