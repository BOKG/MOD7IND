from django.urls import path

from . import views
from .views import TaskListView, CreateTask

urlpatterns = [
    #path('', views.Home.as_view(), name='home')
    path('', views.TaskListView.as_view(), name='home'),
    path('crear_tarea/', views.CreateTask.as_view(), name='crear_tarea'),

]