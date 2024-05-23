# Generated by Django 4.2.10 on 2024-05-23 00:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('service', '0010_alter_user_options_alter_user_managers_user_business_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='location',
        ),
        migrations.AddField(
            model_name='service',
            name='locations',
            field=models.ManyToManyField(related_name='services', to='service.location'),
        ),
        migrations.CreateModel(
            name='ServiceHours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_hours', to='service.service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('contractor', 'Contractor'), ('general', 'General User')], max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.business')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_businesses', to='service.profile'),
        ),
        migrations.AlterField(
            model_name='businessroles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.profile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.profile'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.profile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
