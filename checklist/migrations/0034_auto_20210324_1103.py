# Generated by Django 3.1.7 on 2021-03-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0033_auto_20210324_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(related_name='checklist', to='checklist.ChecklistItem'),
        ),
        migrations.AlterField(
            model_name='checklistscore',
            name='checked',
            field=models.ManyToManyField(related_name='checked', to='checklist.ChecklistItem'),
        ),
    ]
