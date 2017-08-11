# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170811_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_accounts', to='customer.Customer'),
        ),
    ]
