# Generated by Django 2.0.1 on 2018-02-15 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_auto_20180214_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpartyrole',
            name='valid_from',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='valid_from',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='partyroleassociation',
            name='valid_from',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
