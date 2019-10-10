from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task
# from .base_views import DetailView, UpdateView
# Create your views here.


class IndexView(ListView):
    context_object_name = 'tasks'
    template_name = 'task/index.html'
    model = Task
    ordering = '-created_at'
    paginate_by = 2
    paginate_orphans = 1


class TaskView(DetailView):
    context_key = 'tasks'
    model = Task
    template_name = 'task/task.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdate(UpdateView):
    form_class = TaskForm
    template_name = 'task/update.html'
    redirect_url = 'index'
    model = Task
    context_object_name = 'tasks'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDelete(DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('index')


