# Generated by Django 4.2.8 on 2023-12-26 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cancel_reservation', '0002_reservation_delete_cancellation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='table',
        ),
    ]
