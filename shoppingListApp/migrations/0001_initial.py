# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 00:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listName', models.CharField(max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='listEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=50)),
                ('shopName', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('listActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingListApp.list')),
            ],
        ),
    ]
