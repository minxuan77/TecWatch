# Generated by Django 3.1.7 on 2021-03-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0013_auto_20210322_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(to='checklist.ChecklistItem'),
        ),
        migrations.AlterField(
            model_name='checklistscore',
            name='unchecked',
            field=models.ManyToManyField(to='checklist.ChecklistItem'),
        ),
    ]
