# Generated by Django 5.0.6 on 2024-05-26 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0022_auto_20240526_0221"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="locations",
        ),
    ]
