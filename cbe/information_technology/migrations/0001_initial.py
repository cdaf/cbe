# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('documentation', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ComponentClassification',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('documentation', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('logicalresource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resource.LogicalResource')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deployments', to='information_technology.Component')),
            ],
            options={
                'abstract': False,
            },
            bases=('resource.logicalresource',),
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hierarchy_id', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('friendly_name', models.CharField(blank=True, default='', max_length=200)),
                ('documentation', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProcessClassification',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('documentation', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessFramework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('documentation', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='classification',
            field=models.ManyToManyField(blank=True, to='information_technology.ProcessClassification'),
        ),
        migrations.AddField(
            model_name='process',
            name='framework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='information_technology.ProcessFramework'),
        ),
        migrations.AddField(
            model_name='process',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_processes', to='information_technology.Process'),
        ),
        migrations.AddField(
            model_name='component',
            name='classification',
            field=models.ManyToManyField(blank=True, to='information_technology.ComponentClassification'),
        ),
        migrations.AddField(
            model_name='component',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_components', to='information_technology.Component'),
        ),
        migrations.AddField(
            model_name='component',
            name='processes',
            field=models.ManyToManyField(blank=True, related_name='components', to='information_technology.Process'),
        ),
    ]
