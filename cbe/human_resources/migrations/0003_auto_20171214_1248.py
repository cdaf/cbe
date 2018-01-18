# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resource', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('human_resources', '0002_auto_20171214_1248'),
        ('party', '0002_auto_20171214_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='logical_resources',
            field=models.ManyToManyField(blank=True, related_name='human_resources_staff_logical_resources', to='resource.LogicalResource'),
        ),
        migrations.AddField(
            model_name='staff',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='party.Organisation'),
        ),
        migrations.AddField(
            model_name='staff',
            name='physical_contacts',
            field=models.ManyToManyField(blank=True, related_name='human_resources_staff_physical_contacts', to='party.PhysicalContact'),
        ),
        migrations.AddField(
            model_name='staff',
            name='physical_resources',
            field=models.ManyToManyField(blank=True, related_name='human_resources_staff_physical_resources', to='resource.PhysicalResource'),
        ),
        migrations.AddField(
            model_name='staff',
            name='telephone_numbers',
            field=models.ManyToManyField(blank=True, related_name='human_resources_staff_telephone_numbers', to='party.TelephoneNumber'),
        ),
        migrations.AddField(
            model_name='identificationtype',
            name='issuer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='party.Organisation'),
        ),
        migrations.AddField(
            model_name='identification',
            name='identification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resources.IdentificationType'),
        ),
        migrations.AddField(
            model_name='identification',
            name='party_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='human_resources_identification_ownership', to='contenttypes.ContentType'),
        ),
    ]
