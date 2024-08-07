# Generated by Django 4.2.7 on 2024-07-29 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField()),
                ('commentedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentedBy', to=settings.AUTH_USER_MODEL)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loancomment', to='loan.loan')),
            ],
        ),
    ]
