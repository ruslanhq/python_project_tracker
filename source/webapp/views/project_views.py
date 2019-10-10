from django.urls import reverse, reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectList(ListView):
    context_object_name = 'projects'
    template_name = 'project/index.html'
    model = Project
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1


class ProjectView(DetailView):
    pk_url_kwarg = 'pk'
    model = Project
    template_name = 'project/project.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['tasks'] = obj.projects.all().order_by('-created_at')
        return context


class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdate(UpdateView):
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'projects'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDelete(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_object_name = 'projects'
    success_url = reverse_lazy('index')
