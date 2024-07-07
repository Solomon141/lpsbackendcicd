# Generated by Django 4.2.7 on 2024-07-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalId', models.CharField(blank=True, max_length=15, null=True)),
                ('willSaving', models.FloatField(blank=True, default=0, null=True)),
                ('totalSaving', models.FloatField()),
                ('totalShares', models.FloatField()),
                ('isDisbursed', models.BooleanField(default=False)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawloan', to='loan.loan')),
            ],
        ),
    ]