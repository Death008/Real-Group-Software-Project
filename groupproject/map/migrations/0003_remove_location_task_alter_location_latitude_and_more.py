# Generated by Django 5.1.6 on 2025-02-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('map', '0002_rename_quizid_location_challengeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='task',
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='locationId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='qr_code',
            field=models.ImageField(upload_to='qr_codes/'),
        ),
        migrations.AlterField(
            model_name='location',
            name='qr_code_message',
            field=models.CharField(max_length=255),
        ),
    ]
