# Generated by Django 3.1.7 on 2021-03-21 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singhealth', '0033_auto_20210312_1605'),
        ('checklist', '0007_auto_20210314_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklistitem',
            old_name='requirements',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='checklistitem',
            name='type',
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='box',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='CheckListScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(null=True)),
                ('complaint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='singhealth.complaint')),
                ('unchecked', models.ManyToManyField(null=True, to='checklist.CheckListItem')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('F&B', 'F&B'), ('Non F&B', 'Non F&B')], max_length=10, null=True)),
                ('items', models.ManyToManyField(null=True, to='checklist.CheckListItem')),
            ],
        ),
    ]
