from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import Task



class TaskListView(ListView):

    model = Task
    template_name = 'home.html'
    context_object_name = 'tareas'

    def login_required(self):
        if not self.request.user.is_authenticated:
            return redirect('home')
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('due_date')

    # show only task 'IP' or 'P'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.get_queryset().filter(status__in=['IP', 'P'])
        return context
    

class CreateTask(LoginRequiredMixin, CreateView):

    model = Task
    form_class = TaskForm
    template_name = 'tareas/crear_tarea.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    
class DetailsTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tareas/tarea_detalles.html'
    context_object_name = 'tarea'
    fields = ['status']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.get_queryset().first()
        return context

    def post(self, request, *args, **kwargs):
        tarea = self.get_queryset().first()
        tarea.status = request.POST.get('status')
        tarea.status = 'C'
        tarea.save()
        return redirect('home')

class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tareas/editar_tarea.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.get_queryset().first()
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    
class FinishTask(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tareas/tareas_completadas.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('due_date')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # show only task 'c'
        context['tareas'] = self.get_queryset().filter(status__in=['C'])
        return context

@login_required
def delete_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('home')
