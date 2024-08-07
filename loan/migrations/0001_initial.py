# Generated by Django 4.2.7 on 2024-07-29 18:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entityAccountNo', models.CharField(blank=True, max_length=15, null=True)),
                ('expectedDisbursementDate', models.DateField(blank=True, null=True)),
                ('lastReturnDate', models.DateField(blank=True, null=True)),
                ('willSaving', models.FloatField(blank=True, default=0, null=True)),
                ('loanId', models.IntegerField(blank=True, null=True)),
                ('submittedOnDate', models.DateField(default=datetime.date.today)),
                ('totalSaving', models.FloatField()),
                ('totalShares', models.FloatField()),
                ('prcntServiceCharge', models.FloatField(default=8)),
                ('prcntLifeInsurance', models.FloatField(default=3)),
                ('multiplier', models.FloatField(default=4.0)),
                ('flatServiceCharge', models.FloatField(default=0)),
                ('flatLifeInsurance', models.FloatField(default=0)),
                ('tembr', models.FloatField(default=5)),
                ('serviceChargeExtra', models.FloatField(default=0)),
                ('approvedPrincipal', models.FloatField(default=0)),
                ('approvedPrincipalDisbursed', models.FloatField(default=0)),
                ('schFromLoan', models.BooleanField(default=False)),
                ('byDelegation', models.BooleanField(default=False)),
                ('annualInterestRate', models.FloatField(default=0)),
                ('numberOfRepayments', models.IntegerField(blank=True, default=0, null=True)),
                ('totalDueForPeriod', models.FloatField(blank=True, default=0, null=True)),
                ('totalInterestPayment', models.FloatField(blank=True, default=0, null=True)),
                ('queueTime', models.IntegerField(blank=True, default=5, null=True)),
                ('queueDate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('loanProductId', models.IntegerField(blank=True, default=0, null=True)),
                ('loanProductName', models.CharField(blank=True, max_length=255, null=True)),
                ('loanPurposeId', models.IntegerField(blank=True, default=0, null=True)),
                ('loanPurposeName', models.CharField(blank=True, max_length=255, null=True)),
                ('todistributor', models.BooleanField(default=False)),
                ('distributorcomment', models.TextField(blank=True, null=True)),
                ('officerchecking', models.BooleanField(default=False)),
                ('officerapproved', models.BooleanField(default=False)),
                ('officerat', models.DateField(auto_now=True)),
                ('teamleaderchecking', models.BooleanField(default=False)),
                ('teamleaderapproved', models.BooleanField(default=False)),
                ('teamleaderat', models.DateField(auto_now=True)),
                ('auditorchecking', models.BooleanField(default=False)),
                ('auditorapproved', models.BooleanField(default=False)),
                ('auditorat', models.DateField(auto_now=True)),
                ('isDisbursed', models.BooleanField(default=False)),
                ('financeCheking', models.BooleanField(default=False)),
                ('financeapproved', models.BooleanField(default=False)),
                ('financeat', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('assignedTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedTo', to=settings.AUTH_USER_MODEL)),
                ('auditorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auditor', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='customer.customer')),
                ('distributorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributor', to=settings.AUTH_USER_MODEL)),
                ('financeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disbursefinance', to=settings.AUTH_USER_MODEL)),
                ('officerid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Officer', to=settings.AUTH_USER_MODEL)),
                ('submittedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedby', to=settings.AUTH_USER_MODEL)),
                ('teamleaderid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamleader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('loanId', 'customer', 'submittedOnDate')},
            },
        ),
    ]
