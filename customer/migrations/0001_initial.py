# Generated by Django 4.2.7 on 2024-06-09 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entityAccountNo', models.CharField(max_length=255)),
                ('entityExternalId', models.IntegerField()),
                ('activationDate', models.DateField()),
                ('active', models.BooleanField()),
                ('memberSince', models.DateField(default=datetime.date.today)),
                ('displayName', models.CharField(max_length=255)),
                ('amDisplayName', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('amFirstname', models.CharField(max_length=255)),
                ('middlename', models.CharField(max_length=255)),
                ('amMiddlename', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('amLastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=15)),
                ('mobileNo', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('amAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('subcity', models.CharField(blank=True, max_length=255, null=True)),
                ('amSubcity', models.CharField(blank=True, max_length=255, null=True)),
                ('woreda', models.CharField(blank=True, max_length=255, null=True)),
                ('houseNum', models.CharField(blank=True, max_length=255, null=True)),
                ('idNum', models.CharField(blank=True, max_length=255, null=True)),
                ('monthlyIncome', models.FloatField(blank=True, max_length=255, null=True)),
                ('monthlySaving', models.FloatField(blank=True, max_length=255, null=True)),
                ('dateOfBirth', models.DateField()),
                ('isMarried', models.BooleanField()),
                ('isApproved', models.BooleanField(default=False)),
                ('approvedBy', models.BooleanField(default=False)),
                ('approvedAt', models.DateField(blank=True, null=True)),
                ('reviewercomment', models.TextField(blank=True)),
            ],
            options={
                'unique_together': {('entityAccountNo', 'entityExternalId')},
            },
        ),
    ]