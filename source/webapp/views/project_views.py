from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project


class ProjectList(ListView):
    context_object_name = 'projects'
    template_name = 'project/index.html'
    model = Project
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            context['query'] = urlencode({'search': self.search_query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            queryset = queryset.filter(
                Q(name__icontains=self.search_query))
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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
