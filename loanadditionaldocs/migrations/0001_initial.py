# Generated by Django 4.2.7 on 2024-07-19 02:53

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
            name='LoanAdditionalFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileType', models.CharField(blank=True, max_length=25, null=True)),
                ('fileUrl', models.FileField(blank=True, null=True, upload_to='lps_django_2024/uploads/')),
                ('uploadedAt', models.DateField(auto_now_add=True)),
                ('descript', models.TextField()),
                ('isUploaded', models.BooleanField(default=False)),
                ('isApproved', models.BooleanField(default=False)),
                ('approvedAt', models.DateField(blank=True, null=True)),
                ('additionalfiles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanadditionalfiles', to='loan.loan')),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loanadditionalfilesapprove', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loanadditionalfilesuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
