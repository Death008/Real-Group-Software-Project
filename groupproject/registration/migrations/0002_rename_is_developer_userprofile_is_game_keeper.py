# Generated by Django 5.1.6 on 2025-02-16 10:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_developer',
            new_name='is_game_keeper',
        ),
    ]
