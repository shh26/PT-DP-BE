# Generated by Django 5.0.6 on 2024-08-09 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_alter_project_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='scrum_master',
            new_name='lead_developer',
        ),
    ]
