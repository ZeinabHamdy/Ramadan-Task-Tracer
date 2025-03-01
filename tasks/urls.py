from django.urls import path, include
from .views import tasks_view, task_details, add_task, update_task, delete_task

urlpatterns = [
    path('tasks/', tasks_view, name='tasks'),
    path('task/<int:task_id>/', task_details, name='task_details'),
    path('add_task/', add_task, name='add_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),


]
