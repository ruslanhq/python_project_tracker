from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView, CreateView
from .base_views import UpdateView


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

#
# def type_update(request, pk):
#     type = get_object_or_404(Type, pk=pk)
#     if request.method == 'GET':
#         form = TypeForm(data={'type': type.type})
#         return render(request, 'type/type_update.html', context={
#             'form': form,
#             'type': type
#         })
#     elif request.method == 'POST':
#         form = TypeForm(data=request.POST)
#         if form.is_valid():
#             type.status = form.cleaned_data['type']
#             type.type = form.cleaned_data['type']
#             type.save()
#             return redirect('type_list')
#         else:
#             return render(request, 'type/type_update.html', context={
#                 'form': form,
#                 'type': type
#             })


class TypeUpdate(UpdateView):
    form_class = TypeForm
    template_name = 'type/type_update.html'
    redirect_url = 'type_list'
    model = Type
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_list', kwargs={self.pk_kwargs_page: self.object.pk})


def type_delete(request, pk):
    type = get_object_or_404(Type, pk=pk)
    type.delete()
    return redirect('type_list')


