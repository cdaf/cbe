# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_auto_20170811_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_liabilities', to='customer.CustomerAccount'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_liabilities', to='customer.Customer'),
        ),
    ]
