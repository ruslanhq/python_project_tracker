from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView

from webapp.forms import TaskForm
from webapp.models import Task
# Create your views here.


class IndexView(ListView):
    context_object_name = 'tasks'
    template_name = 'task/index.html'
    model = Task
    ordering = '-created_at'
    paginate_by = 2
    paginate_orphans = 1


class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['tasks'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreate(View):
    def get(self, request,  *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/task_create.html', context={
            'form': form
        })

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
            return render(request, 'task/task_create.html', context={'form': form})


class TaskUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={'summary': tasks.summary,
                              'description': tasks.description,
                              'status': tasks.status_id,
                              'type': tasks.type_id}
                        )
        return render(request, 'task/update.html', context={'tasks': tasks, 'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        if form.is_valid():
            tasks.summary = form.cleaned_data['summary']
            tasks.description = form.cleaned_data['description']
            tasks.status = form.cleaned_data['status']
            tasks.type = form.cleaned_data['type']
            tasks.save()
            return redirect('task_view', pk=pk)
        else:
            return render(request, 'task/update.html',
                          context={'form': form,
                                   'tasks': tasks.pk }
                          )


class TaskDelete(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        return render(request, 'task/delete.html', {
            'tasks': tasks
        })

    def post(self, requset, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        tasks.delete()
        return redirect('index')


