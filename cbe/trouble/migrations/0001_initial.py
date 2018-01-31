# Generated by Django 2.0.1 on 2018-01-31 15:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originating_system', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time_raised', models.DateTimeField(auto_now_add=True)),
                ('time_changed', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(max_length=200)),
                ('affected_locations', gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('affected_resources', gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAlarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarmType', models.CharField(max_length=100)),
                ('perceivedSeverity', models.CharField(blank=True, max_length=100, null=True)),
                ('probableCause', models.CharField(blank=True, max_length=100, null=True)),
                ('additionalText', models.TextField(blank=True, null=True)),
                ('alarmReportingTime', models.DateTimeField(auto_now_add=True)),
                ('alarmChangedTime', models.DateTimeField(auto_now=True)),
                ('specificProblem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trouble.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='TrackingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('system', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trouble.Problem')),
                ('resource_alarm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trouble.ResourceAlarm')),
            ],
        ),
        migrations.CreateModel(
            name='TroubleTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('interaction_status', models.CharField(blank=True, max_length=100, null=True)),
                ('place_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('trouble_ticket_state', models.CharField(choices=[('Queued', 'Queued'), ('Active', 'Active'), ('Deferred', 'Deferred'), ('Cleared', 'Cleared'), ('Closed', 'Closed'), ('Disabled', 'Disabled')], max_length=50)),
                ('trouble_detection_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('serviceRestoredDate', models.DateTimeField(blank=True, null=True)),
                ('place_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trouble_troubleticket_place_ownership', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TroubleTicketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_interaction_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('action', models.CharField(blank=True, choices=[('add', 'add'), ('update', 'update'), ('delete', 'delete')], max_length=50, null=True)),
                ('place_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('business_interaction_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trouble_troubleticketitem_interaction_ownership', to='contenttypes.ContentType')),
                ('place_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trouble_troubleticketitem_ownership', to='contenttypes.ContentType')),
                ('trouble_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trouble.TroubleTicket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='problem',
            name='associated_trouble_tickets',
            field=models.ManyToManyField(blank=True, to='trouble.TroubleTicket'),
        ),
        migrations.AddField(
            model_name='problem',
            name='underlying_problems',
            field=models.ManyToManyField(blank=True, to='trouble.Problem'),
        ),
    ]
