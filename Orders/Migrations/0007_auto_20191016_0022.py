# Generated by Django 2.2.5 on 2019-10-15 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191015_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
