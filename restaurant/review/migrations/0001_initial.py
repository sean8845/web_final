# Generated by Django 4.2.8 on 2023-12-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
