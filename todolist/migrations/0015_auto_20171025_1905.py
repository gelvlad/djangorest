# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 16:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0014_auto_20171025_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sharers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]