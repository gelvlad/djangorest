# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0008_auto_20170615_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='sharers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
