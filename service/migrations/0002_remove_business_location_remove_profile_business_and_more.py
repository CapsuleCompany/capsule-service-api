# Generated by Django 4.2.10 on 2024-05-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='business',
        ),
        migrations.AddField(
            model_name='business',
            name='location',
            field=models.ManyToManyField(related_name='locations', to='service.location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='business',
            field=models.ManyToManyField(blank=True, null=True, to='service.business'),
        ),
    ]
