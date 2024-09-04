# Generated by Django 5.0.6 on 2024-07-01 11:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_ms_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ms_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]
