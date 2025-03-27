# Generated by Django 2.2.5 on 2019-10-04 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191004_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItems', to_field='name'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Restaurants', to_field='name'),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
