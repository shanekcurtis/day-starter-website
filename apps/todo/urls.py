from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.create_task, name="create_task"),
    path('delete/<str:todo_id>', views.delete_task, name='delete_task'),
    path('update/<str:todo_id>', views.update_task, name='update_task'),
    path('complete/<str:todo_id>', views.complete_task, name='complete_task')
]