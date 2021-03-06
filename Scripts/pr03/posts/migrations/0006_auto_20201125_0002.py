# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-11-24 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20201124_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['second_name', 'first_name'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('r1', 'Роман'), ('p', 'Поэма'), ('r2', 'Реферат'), ('r3', 'Рассказ')], default='r1', max_length=2, verbose_name='Жанр'),
        ),
    ]
