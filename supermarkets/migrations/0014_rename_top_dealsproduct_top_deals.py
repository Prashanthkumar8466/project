# Generated by Django 5.0.3 on 2024-03-30 09:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0013_alter_order_product_most_sale_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Top_Dealsproduct',
            new_name='Top_Deals',
        ),
    ]
