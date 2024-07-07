# Generated by Django 4.2.7 on 2024-07-07 06:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalId', models.CharField(blank=True, max_length=15, null=True)),
                ('amount', models.FloatField(default=0)),
                ('plannedDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('appointmentDate', models.DateField(blank=True, null=True)),
                ('approvedDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('disbursedDate', models.DateField(blank=True, null=True)),
                ('checkId', models.CharField(blank=True, max_length=255, null=True)),
                ('checkSignedDate', models.DateField(blank=True, null=True)),
                ('isDisbursed', models.BooleanField(default=False)),
                ('approvedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvedby', to=settings.AUTH_USER_MODEL)),
                ('checksignedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checksignedby', to=settings.AUTH_USER_MODEL)),
                ('disbursedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disbursedby', to=settings.AUTH_USER_MODEL)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disbursement_detail', to='loan.loan')),
                ('plannedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plannedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]