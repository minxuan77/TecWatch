# Generated by Django 3.1.7 on 2021-04-04 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0057_auto_20210404_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(related_name='checklist', to='checklist.ChecklistItem'),
        ),
    ]
