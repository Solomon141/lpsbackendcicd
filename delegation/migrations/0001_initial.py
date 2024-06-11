# Generated by Django 4.2.7 on 2024-06-09 03:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('amFullName', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=15)),
                ('mobileNo', models.CharField(max_length=15)),
                ('subcity', models.CharField(blank=True, max_length=255, null=True)),
                ('amSubcity', models.CharField(blank=True, max_length=255, null=True)),
                ('woreda', models.CharField(blank=True, max_length=255, null=True)),
                ('houseNum', models.CharField(blank=True, max_length=255, null=True)),
                ('idnum', models.CharField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateField(default=datetime.date.today)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegatedperson', to='loan.loan')),
            ],
        ),
    ]
