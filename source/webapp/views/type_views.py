from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from .base_views import UpdateView


class TypeView(ListView):
    context_object_name = 'type'
    template_name = 'type/type_list.html'
    model = Type


class TypeCreate(CreateView):
    model = Type
    template_name = 'type/add_type.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_list')


class TypeUpdate(UpdateView):
    form_class = TypeForm
    template_name = 'type/type_update.html'
    redirect_url = 'type_list'
    model = Type
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_list')


class DeleteType(DeleteView):
    model = Type

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('type_list')


