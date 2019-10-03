from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TypeForm
from webapp.models import Type
# Create your views here.


def type_view(request, *args, **kwargs):
    type = Type.objects.all()
    return render(request, 'type/type_list.html', context={
        'type': type
    })


def type_create(request,*args, **kwargs ):
    if request.method == 'GET':
        form = TypeForm()
        return render(request, 'type/add_type.html', context={
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
            return render(request, 'type/add_type.html', context={
                'form': form
            })


def type_update(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        form = TypeForm(data={'type': type.type})
        return render(request, 'type/type_update.html', context={
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
            return render(request, 'type/type_update.html', context={
                'form': form,
                'type': type
            })


def type_delete(request, pk):
    type = get_object_or_404(Type, pk=pk)
    type.delete()
    return redirect('type_list')


