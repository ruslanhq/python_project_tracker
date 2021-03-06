from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from accounts.models import Team
from webapp.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    def __init__(self, project, **kwargs):
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = project.users.all()

    class Meta:
        model = Task
        exclude = ['created_at', 'created_by', 'project']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['updated_at']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


# class ArticleCommentForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['text']
