# Generated by Django 5.0.6 on 2024-08-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_alter_project_general_manager_alter_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='costs',
            name='additional_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='costs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
