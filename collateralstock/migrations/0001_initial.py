# Generated by Django 4.2.7 on 2024-07-29 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan', '0001_initial'),
        ('checklist', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loanguaranteeperson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollateralStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceperstock', models.FloatField()),
                ('stockqty', models.IntegerField()),
                ('letternum', models.CharField(max_length=255)),
                ('letterdate', models.CharField(max_length=255)),
                ('fileType', models.CharField(blank=True, max_length=25, null=True)),
                ('fileUrl', models.FileField(blank=True, null=True, upload_to='lps_django_2024/uploads/')),
                ('uploadedAt', models.DateField(blank=True, null=True)),
                ('isUploaded', models.BooleanField(default=False)),
                ('isApproved', models.BooleanField(default=False)),
                ('approvedAt', models.DateField(blank=True, null=True)),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvedStock', to=settings.AUTH_USER_MODEL)),
                ('bankId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockchecklist', to='checklist.checklist')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collateralstock', to='loan.loan')),
                ('stockgp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stockgp', to='loanguaranteeperson.loanguaranteeperson')),
                ('uploadedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collateralstocksinsertedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
