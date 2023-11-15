# Generated by Django 4.2.2 on 2023-11-11 01:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_authentication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator('^010?[1-9]\\d{3}?\\d{4}$')]),
        ),
    ]
