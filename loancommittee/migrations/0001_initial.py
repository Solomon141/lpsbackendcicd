# Generated by Django 4.2.7 on 2024-07-19 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobposition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enFullName', models.CharField(max_length=255)),
                ('amFullName', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('jobposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobposition', to='jobposition.jonbposition')),
            ],
        ),
    ]
