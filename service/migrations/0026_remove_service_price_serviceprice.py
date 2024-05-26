# Generated by Django 5.0.6 on 2024-05-26 02:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0025_auto_20240526_0226"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="price",
        ),
        migrations.CreateModel(
            name="ServicePrice",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("price", models.FloatField()),
                ("tier", models.CharField(max_length=100)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_prices",
                        to="service.service",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
