# Generated by Django 5.0.3 on 2024-03-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0008_rename_product_recentsearch_recent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentsearch',
            name='recent',
        ),
        migrations.AddField(
            model_name='recentsearch',
            name='recent',
            field=models.ManyToManyField(to='supermarkets.product'),
        ),
    ]
