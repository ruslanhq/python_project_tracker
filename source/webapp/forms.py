from django import forms
from django.forms import widgets

from webapp.models import Status, Type, Task


# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=40, required=True, label='Заголовок')
#     description = forms.CharField(max_length=400, required=False, label='Описание', widget=widgets.Textarea)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус', empty_label=None)
#     type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Тип', empty_label=None)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']

#
# class StatusForm(forms.Form):
#     status = forms.CharField(max_length=10, required=True,  label='Название')


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']
# class TypeForm(forms.Form):
#     type = forms.CharField(max_length=10, required=True, label='Название')
