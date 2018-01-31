# Generated by Django 2.0.1 on 2018-01-31 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('party', '0001_initial'),
        ('project', '0001_initial'),
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetentry',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AddField(
            model_name='timesheetentry',
            name='timesheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_entries', to='human_resources.Timesheet'),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human_resources.Staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='party.Organisation'),
        ),
        migrations.AddField(
            model_name='staff',
            name='email_contacts',
            field=models.ManyToManyField(blank=True, related_name='human_resources_staff_email_contacts', to='party.EmailContact'),
        ),
        migrations.AddField(
            model_name='staff',
            name='individual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='party.Individual'),
        ),
    ]
