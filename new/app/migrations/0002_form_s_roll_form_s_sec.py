# Generated by Django 4.1.4 on 2023-01-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='s_roll',
            field=models.CharField(default=21, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='s_sec',
            field=models.CharField(default=11, max_length=2),
            preserve_default=False,
        ),
    ]