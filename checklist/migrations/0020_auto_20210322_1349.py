# Generated by Django 3.1.7 on 2021-03-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0019_auto_20210322_1347'),
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
