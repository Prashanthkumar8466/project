# Generated by Django 5.0.1 on 2024-02-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("supermarkets", "0002_remove_order_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.TextField(default="Telangana"),
        ),
    ]
