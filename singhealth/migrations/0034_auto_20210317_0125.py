# Generated by Django 3.0.7 on 2021-03-16 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('singhealth', '0033_auto_20210312_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
