# Generated by Django 2.1.3 on 2018-11-16 20:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181116_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]
