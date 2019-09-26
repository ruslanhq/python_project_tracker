from django import forms
from django.forms import widgets

from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=40, required=True, label='Заголовок')
    description = forms.CharField(max_length=400, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус', empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Тип', empty_label=None)


class StatusForm(forms.Form):
    status = forms.CharField(max_length=10, required=True,  label='Название')


class TypeForm(forms.Form):
    type = forms.CharField(max_length=10, required=True, label='Название')
