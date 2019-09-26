from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import TaskForm
from webapp.models import Task
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['tasks'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreate(View):
    def get(self, request,  *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_create.html', context={
            'form': form
        } )

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            tasks = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('task_view', pk=tasks.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})
