# Generated by Django 5.0.2 on 2024-02-08 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global_task_api_app', '0006_infraction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='name',
        ),
    ]