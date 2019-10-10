from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View


class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    pk_kwargs_page = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_pk = kwargs.get(self.pk_kwargs_page)
        context[self.context_key] = get_object_or_404(self.model, pk=name_pk)
        return context


class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_kwargs_page = 'pk'
    context_object_name = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=self.object)
        return render(request, self.template_name, context={'form': form, self.context_object_name: self.object})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance= self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})


# class TaskDelete(View):
#     form_class = None
#     template_name = None
#     redirect_url = ''
#     model = None
#     pk_kwargs_page = 'pk'
#     context_object_name = None
#     confirm = False
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         self.object = get_object_or_404(self.model, pk=pk)
#         form = self.form_class(instance=self.object)
#         if self.confirm == True:
#             return render(request, self.template_name, context={'form': form, self.context_object_name: self.object})
#
#     def post(self, requset, *args, **kwargs):
#         pk = kwargs.get('pk')
#         tasks = get_object_or_404(Task, pk=pk)
#         tasks.delete()
#         return redirect('index')
# НЕ УСПЕЛ.