# Generated by Django 4.2.7 on 2024-07-07 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collateralcar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMarketValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileType', models.CharField(blank=True, max_length=25, null=True)),
                ('fileUrl', models.FileField(blank=True, null=True, upload_to='lps_django_2024/uploads/')),
                ('uploadedAt', models.DateField(auto_now_add=True)),
                ('amDesc', models.CharField(blank=True, default='የገበያ ዋጋ ጥናት ', max_length=255, null=True)),
                ('marketValue', models.FloatField(default=0)),
                ('isUploaded', models.BooleanField(default=False)),
                ('isApproved', models.BooleanField(default=False)),
                ('approvedAt', models.DateField(blank=True, null=True)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mvapprovedBy', to=settings.AUTH_USER_MODEL)),
                ('collateralcar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketvalue', to='collateralcar.collateral_car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marketvalueuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('id', 'collateralcar')},
            },
        ),
    ]
