# Generated by Django 4.2.7 on 2024-07-05 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disbursement', '0003_disbursement_checkid_disbursement_checksignedby_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disbursement',
            old_name='checkSignedBy',
            new_name='checksignedby',
        ),
        migrations.RemoveField(
            model_name='disbursement',
            name='disbursedBy',
        ),
        migrations.AddField(
            model_name='disbursement',
            name='disbursedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disbursedby', to=settings.AUTH_USER_MODEL),
        ),
    ]
