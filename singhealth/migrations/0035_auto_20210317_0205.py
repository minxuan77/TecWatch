# Generated by Django 3.0.7 on 2021-03-16 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('singhealth', '0034_auto_20210317_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant', to=settings.AUTH_USER_MODEL),
        ),
    ]
