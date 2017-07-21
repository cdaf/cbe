# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information_technology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('components', models.ManyToManyField(blank=True, related_name='components', to='information_technology.Component')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
