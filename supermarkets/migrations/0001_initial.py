# Generated by Django 5.0.3 on 2024-03-22 11:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_u',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=12)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Appliance/')),
                ('image_2', models.ImageField(blank=True, upload_to='Appliance/')),
                ('image_3', models.ImageField(blank=True, upload_to='Appliance/')),
                ('image_4', models.ImageField(blank=True, upload_to='Appliance/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_ad3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Appliance/')),
                ('image_2', models.ImageField(blank=True, upload_to='Appliance/')),
                ('image_3', models.ImageField(blank=True, upload_to='Appliance/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('zipcode', models.DecimalField(decimal_places=0, max_digits=6)),
                ('state', models.TextField(default='Telangana')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Electronics_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Electronics/')),
                ('image_2', models.ImageField(blank=True, upload_to='Electronics/')),
                ('image_3', models.ImageField(blank=True, upload_to='Electronics/')),
                ('image_4', models.ImageField(blank=True, upload_to='Electronics/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Electronics_ad3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Electronics/')),
                ('image_2', models.ImageField(blank=True, upload_to='Electronics/')),
                ('image_3', models.ImageField(blank=True, upload_to='Electronics/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Fashion/')),
                ('image_2', models.ImageField(blank=True, upload_to='Fashion/')),
                ('image_3', models.ImageField(blank=True, upload_to='Fashion/')),
                ('image_4', models.ImageField(blank=True, upload_to='Fashion/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion_ad3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='Fashion/')),
                ('image_2', models.ImageField(blank=True, upload_to='Fashion/')),
                ('image_3', models.ImageField(blank=True, upload_to='Fashion/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='furniture_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='furniture/')),
                ('image_2', models.ImageField(blank=True, upload_to='furniture/')),
                ('image_3', models.ImageField(blank=True, upload_to='furniture/')),
                ('image_4', models.ImageField(blank=True, upload_to='furniture/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='furniture_ad3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='furniture/')),
                ('image_2', models.ImageField(blank=True, upload_to='furniture/')),
                ('image_3', models.ImageField(blank=True, upload_to='furniture/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mobile_ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='mobiles/')),
                ('image_2', models.ImageField(blank=True, upload_to='mobiles/')),
                ('image_3', models.ImageField(blank=True, upload_to='mobiles/')),
                ('image_4', models.ImageField(blank=True, upload_to='mobiles/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mobile_ad3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='mobiles/')),
                ('image_2', models.ImageField(blank=True, upload_to='mobiles/')),
                ('image_3', models.ImageField(blank=True, upload_to='mobiles/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.TextField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('category', models.TextField(max_length=20)),
                ('sub_category', models.TextField(blank=True, max_length=20)),
                ('Brand', models.TextField(blank=True, max_length=20)),
                ('product_image', models.ImageField(upload_to='product/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.PositiveSmallIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('on the way', 'on the way'), ('cancel', 'cancel'), ('deliverd', 'deliverd')], default='pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarkets.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarkets.product')),
            ],
        ),
        migrations.CreateModel(
            name='mobile_specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('In_the_Box', models.TextField(blank=True)),
                ('Model_Number', models.TextField(blank=True)),
                ('Model_Name', models.TextField(blank=True)),
                ('Color', models.TextField(blank=True)),
                ('Browse_Type', models.TextField(blank=True)),
                ('Hybrid_Sim_Slot', models.TextField(blank=True)),
                ('Touchscreen', models.TextField(blank=True)),
                ('OTG_Compatible', models.TextField(blank=True)),
                ('Quick_Charging', models.TextField(blank=True)),
                ('Display_Size', models.TextField(blank=True)),
                ('Resolution', models.TextField(blank=True)),
                ('Resolution_Type', models.TextField(blank=True)),
                ('GPU', models.TextField(blank=True)),
                ('Display_Type', models.TextField(blank=True)),
                ('Display_Colors', models.TextField(blank=True)),
                ('Other_Display_Features', models.TextField(blank=True)),
                ('SIM_Type', models.TextField(blank=True)),
                ('Operating_System', models.TextField(blank=True)),
                ('Processor_Brand', models.TextField(blank=True)),
                ('Processor_Type', models.TextField(blank=True)),
                ('Processor_Core', models.TextField(blank=True)),
                ('Primary_Clock_Speed', models.TextField(blank=True)),
                ('Secondary_Clock_Speed', models.TextField(blank=True)),
                ('Operating_Frequency', models.TextField(blank=True)),
                ('Internal_Storage', models.TextField(blank=True)),
                ('RAM', models.TextField(blank=True)),
                ('Primary_Camera_Available', models.TextField(blank=True)),
                ('Primary_Camera_Features', models.TextField(blank=True)),
                ('Optical_Zoom', models.TextField(blank=True)),
                ('Secondary_Camera_Available', models.TextField(blank=True)),
                ('Secondary_Camera', models.TextField(blank=True)),
                ('Secondary_Camera_Features', models.TextField(blank=True)),
                ('Flash', models.TextField(blank=True)),
                ('HD_Recording', models.TextField(blank=True)),
                ('Full_HD_Recording', models.TextField(blank=True)),
                ('Video_Recording', models.TextField(blank=True)),
                ('Video_Recording_Resolution', models.TextField(blank=True)),
                ('Digital_Zoom', models.TextField(blank=True)),
                ('Frame_Rate', models.TextField(blank=True)),
                ('Dual_Camera_Lens', models.TextField(blank=True)),
                ('Video_Call_Support', models.TextField(blank=True)),
                ('Speaker_Phone', models.TextField(blank=True)),
                ('Call_Records', models.TextField(blank=True)),
                ('Network_Type', models.TextField(blank=True)),
                ('Supported_Networks', models.TextField(blank=True)),
                ('Internet_Connectivity', models.TextField(blank=True)),
                ('ThreeG', models.TextField(blank=True)),
                ('GPRS', models.TextField(blank=True)),
                ('Micro_USB_Version', models.TextField(blank=True)),
                ('Bluetooth_Support', models.TextField(blank=True)),
                ('Bluetooth_Version', models.TextField(blank=True)),
                ('Wi_Fi', models.TextField(blank=True)),
                ('Wi_Fi_Version', models.TextField(blank=True)),
                ('Wi_Fi_Hotspot', models.TextField(blank=True)),
                ('NFC', models.TextField(blank=True)),
                ('Infrared', models.TextField(blank=True)),
                ('USB_Connectivity', models.TextField(blank=True)),
                ('EDGE', models.TextField(blank=True)),
                ('Audio_Jack', models.TextField(blank=True)),
                ('Map_Support', models.TextField(blank=True)),
                ('GPS_Support', models.TextField(blank=True)),
                ('Smartphone', models.TextField(blank=True)),
                ('Touchscreen_Type', models.TextField(blank=True)),
                ('SIM_Size', models.TextField(blank=True)),
                ('User_Interface', models.TextField(blank=True)),
                ('SMS', models.TextField(blank=True)),
                ('Graphics_PPI', models.TextField(blank=True)),
                ('Sensors', models.TextField(blank=True)),
                ('Ringtones_Format', models.TextField(blank=True)),
                ('Other_Features', models.TextField(blank=True)),
                ('GPS_Type', models.TextField(blank=True)),
                ('FM_Radio', models.TextField(blank=True)),
                ('DLNA_Support', models.TextField(blank=True)),
                ('Audio_Formats', models.TextField(blank=True)),
                ('Video_Formats', models.TextField(blank=True)),
                ('Battery_Capacity', models.TextField(blank=True)),
                ('Battery_Type', models.TextField(blank=True)),
                ('Width', models.TextField(blank=True)),
                ('Height', models.TextField(blank=True)),
                ('Depth', models.TextField(blank=True)),
                ('Weight', models.TextField(blank=True)),
                ('Warranty_Summary', models.TextField(blank=True)),
                ('Domestic_Warranty', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='supermarkets.product')),
            ],
        ),
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cart_items', models.ManyToManyField(to='supermarkets.product')),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wish_item', models.ManyToManyField(to='supermarkets.product')),
            ],
        ),
    ]
