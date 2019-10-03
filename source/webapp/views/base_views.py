from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    pk_kwargs_page = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_pk = kwargs.get(self.pk_kwargs_page)
        context[self.context_key] = get_object_or_404(self.model, pk=name_pk)
        return context

