# Generated by Django 5.0.2 on 2024-02-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_task_api_app', '0004_officer_last_login_officer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]