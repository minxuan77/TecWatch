# Generated by Django 3.1.7 on 2021-03-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singhealth', '0009_auto_20210305_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
