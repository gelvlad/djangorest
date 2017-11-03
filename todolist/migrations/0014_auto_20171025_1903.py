# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 16:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0013_tasklist_sharers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sharers',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
