# Generated by Django 5.0.6 on 2024-06-02 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='descripto',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='markal',
            new_name='marka',
        ),
    ]
