# Generated by Django 3.2.7 on 2021-09-08 23:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210908_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextrainfo',
            name='registered_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
