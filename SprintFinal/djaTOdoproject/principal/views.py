from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from .forms import TaskForm
from .models import Task


class Home(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class TaskListView(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tareas/principal_tareas.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.get_queryset().filter(status__in=['IP', 'P'])

        # filter by status or label
        if self.request.GET.get('status'):
            context['tareas'] = context['tareas'].filter(
                status=self.request.GET.get('status'))
        if self.request.GET.get('label_id'):
            context['tareas'] = context['tareas'].filter(
                label_id=self.request.GET.get('label_id'))
        if self.request.GET.get('priority'):
            context['tareas'] = context['tareas'].filter(
                priority=self.request.GET.get('priority'))
        return context


class CreateTask(LoginRequiredMixin, CreateView):

    model = Task
    form_class = TaskForm
    template_name = 'tareas/crear_tarea.html'
    success_url = reverse_lazy('principal_tareas')

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.instance.user = User.objects.get(
                id=self.request.POST.get('user'))
            return super().form_valid(form)
        else:
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
        return redirect('principal_tareas')


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tareas/editar_tarea.html'
    success_url = reverse_lazy('principal_tareas')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.get_queryset().first()
        return context

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.instance.user = User.objects.get(
                id=self.request.POST.get('user'))
            return super().form_valid(form)
        else:
            print(form.errors)
            return super().form_valid(form)

    # Si el usuario es admin, puede editar cualquier tarea
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            tarea = self.get_queryset().first()
            if tarea.user == request.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('principal_tareas')

    # Si el usuario es no es admin, solo puede editar sus tareas
    def get_success_url(self):
        if self.request.user.is_superuser:
            return super().get_success_url()
        else:
            return reverse_lazy('principal_tareas')


class FinishTask(LoginRequiredMixin, ListView):

    model = Task
    template_name = 'tareas/tareas_completadas.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = self.get_queryset().filter(status__in=['C'])

        # filter by status or label
        if self.request.GET.get('status'):
            context['tareas'] = context['tareas'].filter(
                status=self.request.GET.get('status'))
        if self.request.GET.get('label_id'):
            context['tareas'] = context['tareas'].filter(
                label_id=self.request.GET.get('label_id'))
        if self.request.GET.get('priority'):
            context['tareas'] = context['tareas'].filter(
                priority=self.request.GET.get('priority'))
        return context


@login_required
def delete_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('principal_tareas')
