# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='party_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='party_user',
        ),
    ]