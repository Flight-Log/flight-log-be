# Generated by Django 4.2.3 on 2023-07-07 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_log_be', '0002_flight'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Flight',
        ),
    ]