from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import TaskForm, StatusForm, TypeForm
from webapp.models import Task, Status, Type
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


class TaskUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={'summary': tasks.summary,
                              'description': tasks.description,
                              'status': tasks.status_id,
                              'type': tasks.type_id}
                        )
        return render(request, 'update.html', context={'tasks': tasks, 'form': form})

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
            return render(request, 'update.html',
                          context={'form': form,
                                   'tasks': tasks.pk }
                          )


class TaskDelete(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        return render(request, 'delete.html', {
            'tasks': tasks
        })

    def post(self, requset, *args, **kwargs):
        pk = kwargs.get('pk')
        tasks = get_object_or_404(Task, pk=pk)
        tasks.delete()
        return redirect('index')


def status_view(request, *args, **kwargs):
    status = Status.objects.all()
    return render(request, 'status_list.html', context={
        'status': status
    })


def type_view(request, *args, **kwargs):
    type = Type.objects.all()
    return render(request, 'type_list.html', context={
        'type': type
    })


def status_create(request,*args, **kwargs ):
    if request.method == 'GET':
        form = StatusForm()
        return render(request, 'add_status.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_list')
        else:
            return render(request, 'add_status.html', context={
                'form': form
            })


def type_create(request,*args, **kwargs ):
    if request.method == 'GET':
        form = TypeForm()
        return render(request, 'add_type.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('type_list')
        else:
            return render(request, 'add_type.html', context={
                'form': form
            })


def status_update(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={'status': status.status})
        return render(request, 'status_update.html', context={
            'form': form,
            'status': status
        })
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['status']
            status.save()
            return redirect('status_list')
        else:
            return render(request, 'status_update.html', context={
                'form': form,
                'status': status
            })


def type_update(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        form = TypeForm(data={'type': type.type})
        return render(request, 'type_update.html', context={
            'form': form,
            'type': type
        })
    elif request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.status = form.cleaned_data['type']
            type.type = form.cleaned_data['type']
            type.save()
            return redirect('type_list')
        else:
            return render(request, 'type_update.html', context={
                'form': form,
                'type': type
            })


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('status_list')


def type_delete(request, pk):
    type = get_object_or_404(Type, pk=pk)
    type.delete()
    return redirect('type_list')


