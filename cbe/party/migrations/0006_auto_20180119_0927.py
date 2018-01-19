# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0005_auto_20180117_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='enterprise_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
