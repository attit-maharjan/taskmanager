from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task-list'),
    path('create/', task_create, name='task-create'),
    path('update/<int:task_id>/', task_update, name='task-update'),
    path('delete/<int:task_id>/', task_delete, name='task-delete'),
]
