# Generated by Django 5.0.2 on 2024-03-01 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_specification',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='supermarkets.product'),
        ),
    ]