# Generated by Django 5.0.3 on 2024-04-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0022_remove_cart_add_at_remove_cart_cart_items_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='product',
        ),
    ]
