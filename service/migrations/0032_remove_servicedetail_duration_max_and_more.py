# Generated by Django 5.0.6 on 2024-05-26 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0031_auto_20240526_0234"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicedetail",
            name="duration_max",
        ),
        migrations.RemoveField(
            model_name="servicedetail",
            name="duration_min",
        ),
        migrations.AddField(
            model_name="serviceprice",
            name="service_detail",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_prices",
                to="service.servicedetail",
            ),
        ),
        migrations.AlterField(
            model_name="serviceprice",
            name="service",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_prices",
                to="service.service",
            ),
        ),
    ]
