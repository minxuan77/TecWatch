# Generated by Django 3.1.7 on 2021-03-12 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singhealth', '0030_complaint_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Edit_Complaint',
            new_name='Response',
        ),
    ]