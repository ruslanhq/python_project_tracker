from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project


# Create your views here.


class IndexView(ListView):
    context_object_name = 'tasks'
    template_name = 'task/index.html'
    model = Task
    ordering = '-created_at'
    paginate_by = 2
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
                Q(summary__icontains=self.search_query)
                | Q(description__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(DetailView):
    pk_url_kwarg = 'pk'
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'tasks'


class TaskCreate(UserPassesTestMixin, CreateView):
    model = Task
    template_name = 'task/task_create.html'
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = self.get_project()
        return kwargs

    def test_func(self):
        project = self.get_project()
        users = project.users.all()
        if self.request.user in users:
            return True
        else:
            return False

    def get_project(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.project = self.get_project()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdate(UserPassesTestMixin, UpdateView):
    form_class = TaskForm
    template_name = 'task/update.html'
    model = Task
    context_object_name = 'tasks'

    def test_func(self):
        project = self.get_object().project
        users = project.users.all()
        if self.request.user in users:
            return True
        else:
            return False

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDelete(UserPassesTestMixin, DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('index')

    def test_func(self):
        project = self.get_object().project
        users = project.users.all()
        if self.request.user in users:
            return True
        else:
            return False





