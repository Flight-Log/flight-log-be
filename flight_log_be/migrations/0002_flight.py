# Generated by Django 4.2.3 on 2023-07-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_log_be', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]