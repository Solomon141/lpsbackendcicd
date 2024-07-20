# Generated by Django 4.2.7 on 2024-07-19 02:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('withdrawal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('plannedDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('appointmentDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('checkId', models.CharField(blank=True, max_length=255, null=True)),
                ('checksignedby', models.TextField(blank=True, null=True)),
                ('checkIssuedDate', models.DateField(blank=True, null=True)),
                ('isDisbursed', models.BooleanField(default=False)),
                ('checkissuedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdrawalcheckissuedby', to=settings.AUTH_USER_MODEL)),
                ('disbursedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdrawaldisbursedby', to=settings.AUTH_USER_MODEL)),
                ('plannedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdrawalplannedby', to=settings.AUTH_USER_MODEL)),
                ('withdrawal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal', to='withdrawal.withdrawal')),
            ],
        ),
    ]
