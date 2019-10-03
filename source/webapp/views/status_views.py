from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView
# Create your views here.


class StatusView(ListView):
    context_object_name = 'status'
    template_name = 'status/status_list.html'
    model = Status


def status_create(request,*args, **kwargs ):
    if request.method == 'GET':
        form = StatusForm()
        return render(request, 'status/add_status.html', context={
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
            return render(request, 'status/add_status.html', context={
                'form': form
            })


def status_update(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={'status': status.status})
        return render(request, 'status/status_update.html', context={
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
            return render(request, 'status/status_update.html', context={
                'form': form,
                'status': status
            })


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('status_list')





