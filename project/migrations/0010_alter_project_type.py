# Generated by Django 5.0.6 on 2024-07-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(blank=True, choices=[('Data', 'Data'), ('Application', 'Application')], max_length=50, null=True),
        ),
    ]
