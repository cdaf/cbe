# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('human_resources', '0004_staff_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='identification',
            name='party_role_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='human_resources_identification_party_role_identifiers', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='identification',
            name='party_role_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='identification',
            name='party_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='human_resources_identification_party_identifiers', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='identification',
            name='party_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
