# Generated by Django 3.0.7 on 2021-04-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0062_auto_20210405_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(related_name='checklist', to='checklist.ChecklistItem'),
        ),
    ]