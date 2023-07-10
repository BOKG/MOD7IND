from django.urls import path
from . import views
from .views import delete_task

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('tareas/', views.TaskListView.as_view(), name='principal_tareas'),
    path('crear_tarea/', views.CreateTask.as_view(), name='crear_tarea'),
    path('tarea/<int:pk>/', views.DetailsTask.as_view(), name='tarea_detalles'),
    path('tarea/<int:pk>/editar/', views.EditTask.as_view(), name='editar_tarea'),
    path('finalizar/', views.FinishTask.as_view(), name='complete_task'),
    path('tarea/<int:pk>/eliminar/', delete_task, name='eliminar_tarea'),
]
