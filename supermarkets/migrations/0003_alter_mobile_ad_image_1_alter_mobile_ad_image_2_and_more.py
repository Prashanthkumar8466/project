# Generated by Django 5.0.3 on 2024-03-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarkets', '0002_alter_mobile_specification_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_ad',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad3',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad3',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile_ad3',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='mobiles/'),
        ),
    ]