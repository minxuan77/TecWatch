# Generated by Django 3.1.7 on 2021-03-25 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0040_auto_20210325_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistscore',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
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