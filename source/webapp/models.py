from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def get_admin():
    return User.objects.get(username='admin').id


class Task(models.Model):
    summary = models.CharField(max_length=40, verbose_name='Заголовок')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', related_name='types', on_delete=models.PROTECT, verbose_name='Тип')
    project = models.ForeignKey('webapp.Project', related_name='projects', on_delete=models.PROTECT, null=True,
                                blank=False, verbose_name='Проект')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey(User, null=False, blank=False, default=get_admin, verbose_name='Автор задачи',
                                   on_delete=models.PROTECT, related_name='c_tasks')
    assigned_to = models.ForeignKey(User, null=False, blank=False, default=get_admin, verbose_name='Исполнитель задачи',
                                    on_delete=models.PROTECT, related_name='a_tasks')

    def __str__(self):
        return self.summary


class Status(models.Model):
    status = models.CharField(max_length=10, verbose_name='Статус')

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=10, verbose_name='Тип')

    def __str__(self):
        return self.type


class Project(models.Model):
    name = models.CharField(max_length=17, verbose_name='Название проекта')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    users = models.ManyToManyField(User, through='accounts.Team', through_fields=('project', 'user'),
                                   related_name='projects', verbose_name='Пользователи')

    def __str__(self):
        return self.name

    



