# Generated by Django 3.1.7 on 2021-03-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singhealth', '0004_outlet_tenants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tenants',
            new_name='Tenant',
        ),
    ]
