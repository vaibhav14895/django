# Generated by Django 4.1.4 on 2023-01-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_form_s_roll_form_s_sec'),
    ]

    operations = [
        migrations.CreateModel(
            name='forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('s_roll', models.IntegerField()),
                ('s_sec', models.IntegerField()),
                ('s_CGPA', models.IntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='form',
        ),
    ]
