# Generated by Django 2.2 on 2019-11-04 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_auto_20191010_1059'),
        ('accounts', '0003_auto_20191104_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Датасоздания')),
                ('date_finish', models.DateTimeField(verbose_name='Дата окончания')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_projects', to='webapp.Project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
