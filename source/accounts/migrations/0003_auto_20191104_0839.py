# Generated by Django 2.2 on 2019-11-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191103_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='profile',
            name='git',
            field=models.URLField(blank=True, null=True, verbose_name='Профиль github'),
        ),
    ]
