# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-31 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('physical_object', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urbanpropertysubaddress',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='physical_object.Structure'),
        ),
        migrations.AddField(
            model_name='urbanpropertysubaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City'),
        ),
        migrations.AddField(
            model_name='urbanpropertysubaddress',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='urbanpropertysubaddress',
            name='urban_property_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.UrbanPropertyAddress'),
        ),
        migrations.AddField(
            model_name='urbanpropertyaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City'),
        ),
        migrations.AddField(
            model_name='urbanpropertyaddress',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='ruralpropertysubaddress',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='physical_object.Structure'),
        ),
        migrations.AddField(
            model_name='ruralpropertysubaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City'),
        ),
        migrations.AddField(
            model_name='ruralpropertysubaddress',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='ruralpropertysubaddress',
            name='rural_property_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.RuralPropertyAddress'),
        ),
        migrations.AddField(
            model_name='ruralpropertyaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City'),
        ),
        migrations.AddField(
            model_name='ruralpropertyaddress',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='poboxaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City'),
        ),
        migrations.AddField(
            model_name='poboxaddress',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
        migrations.AddField(
            model_name='location',
            name='geographic_address_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_location_ownership', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Country'),
        ),
    ]
