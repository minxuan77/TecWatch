# Generated by Django 3.2 on 2021-04-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0070_alter_checklist_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(related_name='checklist', to='checklist.ChecklistItem'),
        ),
    ]
