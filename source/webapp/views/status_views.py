from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from .base_views import UpdateView


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


class StatusUpdate(UpdateView):
    form_class = StatusForm
    template_name = 'status/status_update.html'
    redirect_url = 'status_list'
    model = Status
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_list', kwargs={'pk': self.object.pk})


class StatusDelete(DeleteView):
    model = Status

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('status_list', kwargs={'pk':self.object.pk})
