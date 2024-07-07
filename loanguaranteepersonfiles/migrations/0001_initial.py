# Generated by Django 4.2.7 on 2024-07-07 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loanguaranteeperson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanGuaranteePersonFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileType', models.CharField(blank=True, max_length=25, null=True)),
                ('fileUrl', models.FileField(blank=True, null=True, upload_to='lps_django_2024/uploads/')),
                ('uploadedAt', models.DateField(auto_now_add=True)),
                ('amDesc', models.CharField(blank=True, max_length=255, null=True)),
                ('guaranteeperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanguaranteeperson', to='loanguaranteeperson.loanguaranteeperson')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guaranteepersonuploaduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
