# Generated by Django 3.1.7 on 2021-03-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_auto_20210314_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='type',
            field=models.CharField(choices=[('F&B', 'F&B'), ('Others', 'Others'), ('Both', 'Both')], max_length=10, null=True),
        ),
    ]
