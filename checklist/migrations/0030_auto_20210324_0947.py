# Generated by Django 3.1.7 on 2021-03-24 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singhealth', '0036_remove_complaint_score'),
        ('checklist', '0029_auto_20210322_1739'),
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
        migrations.AlterField(
            model_name='checklistscore',
            name='complaint',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score', to='singhealth.complaint'),
        ),
    ]