# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-11-24 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201124_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]