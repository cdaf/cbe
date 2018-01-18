# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('information_technology', '0002_auto_20171214_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='processes',
            field=models.ManyToManyField(blank=True, related_name='projects', to='information_technology.Process'),
        ),
    ]
