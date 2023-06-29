from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import TaskForm
from .models import Task
# Create your views here.
# class Home(ListView):
#     def get(self, request):
#         return render(request, 'home.html', {})
    
class TaskListView(ListView):

    model = Task
    template_name = 'home.html'
    context_object_name = 'tareas'



    def get_queryset(self):
        queryset = super().get_queryset()
        etiqueta = self.request.GET.get('etiqueta')
        estado = self.request.GET.get('estado')

        if etiqueta:
            queryset = queryset.filter(etiquetas__nombre=etiqueta)

        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset.order_by('due_date')
    

class CreateTask(LoginRequiredMixin, CreateView):

    model = Task
    form_class = TaskForm
    template_name = 'tareas/crear_tarea.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)