# Generated by Django 4.2.7 on 2024-06-16 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearRange', models.CharField(max_length=255)),
                ('multiplierRatio', models.FloatField()),
            ],
        ),
    ]
