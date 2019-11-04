from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    about_me = models.TextField(null=True, blank=True, max_length=200, verbose_name='О себе')
    git = models.URLField(verbose_name='Профиль github', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Team(models.Model):
    user = models.ForeignKey('auth.User', related_name='team_user', on_delete=models.CASCADE, verbose_name='Пользователь')
    project = models.ForeignKey('webapp.Project', related_name='team_projects', on_delete=models.CASCADE, verbose_name='Проект')
    date_start = models.DateTimeField(verbose_name='Датасоздания')
    date_finish = models.DateTimeField(verbose_name='Дата окончания')

    def __str__(self):
        return '{} | {}'.format(self.user, self.project)

