# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='slug',
            field=models.CharField(default='shopping-list', max_length=300),
            preserve_default=False,
        ),
    ]
