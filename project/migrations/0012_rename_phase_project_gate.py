# Generated by Django 5.0.6 on 2024-07-31 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_costs_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='phase',
            new_name='gate',
        ),
    ]
