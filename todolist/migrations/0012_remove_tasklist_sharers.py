# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_tasklist_sharers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='sharers',
        ),
    ]