# Generated by Django 3.1.7 on 2021-03-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0049_auto_20210326_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='items',
            field=models.ManyToManyField(related_name='checklist', to='checklist.ChecklistItem'),
        ),
    ]
