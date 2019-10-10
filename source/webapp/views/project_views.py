from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectList(ListView):
    context_object_name = 'projects'
    template_name = 'project/index.html'
    model = Project
    ordering = '-created_at'
    paginate_by = 2
    paginate_orphans = 1


class ProjectView(DetailView):
    pk_url_kwarg = 'pk'
    model = Project
    template_name = 'project/project.html'
    context_object_name = 'projects'
