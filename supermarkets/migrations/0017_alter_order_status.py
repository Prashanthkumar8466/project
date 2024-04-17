# Generated by Django 5.0.3 on 2024-04-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0016_rename_festivalproduct_festival_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Confirmed', 'Order Confirmed'), ('Out For Delivery', 'Out For Delivery'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Return', 'Return'), ('Refund completed', 'Refund completed'), ('Packing', 'Packing')], default='pending', max_length=50),
        ),
    ]