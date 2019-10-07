from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView
from .base_views import UpdateView


# Create your views here.


class StatusView(ListView):
    context_object_name = 'status'
    template_name = 'status/status_list.html'
    model = Status


class StatusCreate(CreateView):
    model = Status
    template_name = 'status/add_status.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_list')

#
# def status_update(request, pk):
#     status = get_object_or_404(Status, pk=pk)
#     if request.method == 'GET':
#         form = StatusForm(data={'status': status.status})
#         return render(request, 'status/status_update.html', context={
#             'form': form,
#             'status': status
#         })
#     elif request.method == 'POST':
#         form = StatusForm(data=request.POST)
#         if form.is_valid():
#             status.status = form.cleaned_data['status']
#             status.save()
#             return redirect('status_list')
#         else:
#             return render(request, 'status/status_update.html', context={
#                 'form': form,
#                 'status': status
#             })


class StatusUpdate(UpdateView):
    form_class = StatusForm
    template_name = 'status/status_update.html'
    redirect_url = 'status_list'
    model = Status
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_list', kwargs={self.pk_kwargs_page: self.object.pk})


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('status_list')
