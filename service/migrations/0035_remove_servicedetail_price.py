# Generated by Django 5.0.6 on 2024-05-26 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0034_auto_20240526_0234"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicedetail",
            name="price",
        ),
    ]
