# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0007_auto_20170613_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='user',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasklists', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
