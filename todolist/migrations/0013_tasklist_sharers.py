# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0012_remove_tasklist_sharers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='sharers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
