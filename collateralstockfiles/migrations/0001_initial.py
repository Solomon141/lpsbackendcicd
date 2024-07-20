# Generated by Django 4.2.7 on 2024-07-19 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collateralstock', '0001_initial'),
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollateralStockFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileType', models.CharField(blank=True, max_length=25, null=True)),
                ('fileUrl', models.FileField(blank=True, null=True, upload_to='lps_django_2024/uploads/')),
                ('uploadedAt', models.DateField(auto_now_add=True)),
                ('amDesc', models.CharField(blank=True, max_length=255, null=True)),
                ('isUploaded', models.BooleanField(default=False)),
                ('isMandatory', models.BooleanField(default=True)),
                ('checkListId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockfileschecklist', to='checklist.checklist')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockfiles', to='collateralstock.collateralstock')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collateralstockuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
