# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_auto_20180117_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]