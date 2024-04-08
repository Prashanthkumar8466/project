
from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
STATUS_CHOICE=[
    ('Pending','Pending'),
   ('Out For Delivery','Out For Delivery'),
    ('Cancel','Cancel'),
    ('Deliverd','Deliverd'),
    ('Return','Return'),
    ('Refund completed','Refund completed'),
    ('Packing','Packing')
]
#categories
class product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productname=models.TextField(max_length=100)
    price=models.FloatField()
    discount=models.FloatField(default=0)
    description=models.TextField()
    category = models.TextField(max_length=20)
    sub_category= models.TextField(max_length=20,blank=True)
    Brand = models.TextField(max_length=20,blank=True)
    product_image=models.ImageField(upload_to='product/')
    def __str__(self):
        return self.productname
#mobiles
class mobile_specification(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.OneToOneField(product,on_delete=models.CASCADE)
    In_the_Box=models.TextField(blank=True)
    Model_Number=models.TextField(blank=True)
    Model_Name=models.TextField(blank=True)
    Color=models.TextField(blank=True)
    Browse_Type=models.TextField(blank=True)
    SIM_Type=models.TextField(blank=True)
    Hybrid_Sim_Slot=models.TextField(blank=True)
    SIM_Type=models.TextField(blank=True)
    Touchscreen=models.TextField(blank=True)
    OTG_Compatible=models.TextField(blank=True)
    Quick_Charging=models.TextField(blank=True)
    Display_Size=models.TextField(blank=True)
    Resolution=models.TextField(blank=True)
    Resolution_Type=models.TextField(blank=True)
    GPU=models.TextField(blank=True)
    Display_Type=models.TextField(blank=True)
    Display_Colors=models.TextField(blank=True)
    Other_Display_Features=models.TextField(blank=True)
    SIM_Type=models.TextField(blank=True)
    Operating_System=models.TextField(blank=True)
    Processor_Brand=models.TextField(blank=True)
    Processor_Type=models.TextField(blank=True)
    Processor_Core=models.TextField(blank=True)
    Primary_Clock_Speed=models.TextField(blank=True)
    Secondary_Clock_Speed=models.TextField(blank=True)
    Operating_Frequency=models.TextField(blank=True)
    Internal_Storage=models.TextField(blank=True)
    RAM=models.TextField(blank=True)
    Primary_Camera_Available=models.TextField(blank=True)
    Primary_Camera_Features=models.TextField(blank=True)
    Optical_Zoom=models.TextField(blank=True)
    Secondary_Camera_Available=models.TextField(blank=True)
    Secondary_Camera=models.TextField(blank=True)
    Secondary_Camera_Features=models.TextField(blank=True)
    Flash=models.TextField(blank=True)
    HD_Recording=models.TextField(blank=True)
    Full_HD_Recording=models.TextField(blank=True)
    Video_Recording=models.TextField(blank=True)
    Video_Recording_Resolution=models.TextField(blank=True)
    Digital_Zoom=models.TextField(blank=True)
    Frame_Rate=models.TextField(blank=True)
    Dual_Camera_Lens=models.TextField(blank=True)
    Video_Call_Support=models.TextField(blank=True)
    Speaker_Phone=models.TextField(blank=True)
    Call_Records=models.TextField(blank=True)
    Network_Type=models.TextField(blank=True)
    Supported_Networks=models.TextField(blank=True)
    Internet_Connectivity=models.TextField(blank=True)
    ThreeG=models.TextField(blank=True)
    GPRS=models.TextField(blank=True)
    Micro_USB_Version=models.TextField(blank=True)
    Bluetooth_Support=models.TextField(blank=True)
    Bluetooth_Version=models.TextField(blank=True)
    Wi_Fi=models.TextField(blank=True)
    Wi_Fi_Version=models.TextField(blank=True)
    Wi_Fi_Hotspot=models.TextField(blank=True)
    NFC=models.TextField(blank=True)
    Infrared=models.TextField(blank=True)
    USB_Connectivity=models.TextField(blank=True)
    EDGE=models.TextField(blank=True)
    Audio_Jack=models.TextField(blank=True)
    Map_Support=models.TextField(blank=True)
    GPS_Support=models.TextField(blank=True)
    Smartphone=models.TextField(blank=True)
    Touchscreen_Type=models.TextField(blank=True)
    SIM_Size=models.TextField(blank=True)
    User_Interface=models.TextField(blank=True)
    SMS=models.TextField(blank=True)
    Graphics_PPI=models.TextField(blank=True)
    Sensors=models.TextField(blank=True)
    Ringtones_Format=models.TextField(blank=True)
    Other_Features=models.TextField(blank=True)
    GPS_Type=models.TextField(blank=True)
    FM_Radio=models.TextField(blank=True)
    DLNA_Support=models.TextField(blank=True)
    Audio_Formats=models.TextField(blank=True)
    Video_Formats=models.TextField(blank=True)
    Battery_Capacity=models.TextField(blank=True)
    Battery_Type=models.TextField(blank=True)
    Width=models.TextField(blank=True)
    Height=models.TextField(blank=True)
    Depth=models.TextField(blank=True)
    Weight=models.TextField(blank=True)
    Warranty_Summary=models.TextField(blank=True)
    Domestic_Warranty=models.TextField(blank=True)
class contact_u(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.TextField()
    city=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    zipcode=models.DecimalField(max_digits=6,decimal_places=0)
    state=models.TextField(default='Telangana')
    def __str__(self):
        return self.name
class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=timezone.now)
    wish_item=models.ManyToManyField('product')
    add_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'wishlist for {self.user.username}'
class cart_item(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cart_items=models.ManyToManyField(product)
    add_at=models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f'cart items of {self.user.username}'
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField(default=0)
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)
class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quality=models.PositiveSmallIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')
    amountpaid=models.IntegerField(blank=True)
    othercharges=models.IntegerField(blank=True)
    #payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
class mobile_ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='mobiles/',blank=True)
    image_2=models.ImageField(upload_to='mobiles/',blank=True)
    image_3=models.ImageField(upload_to='mobiles/',blank=True)
    image_4=models.ImageField(upload_to='mobiles/',blank=True)
class mobile_ad3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='mobiles/',blank=True)
    image_2=models.ImageField(upload_to='mobiles/',blank=True)
    image_3=models.ImageField(upload_to='mobiles/',blank=True)
class Appliance_ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Appliance/',blank=True)
    image_2=models.ImageField(upload_to='Appliance/',blank=True)
    image_3=models.ImageField(upload_to='Appliance/',blank=True)
    image_4=models.ImageField(upload_to='Appliance/',blank=True)
class Appliance_ad3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Appliance/',blank=True)
    image_2=models.ImageField(upload_to='Appliance/',blank=True)
    image_3=models.ImageField(upload_to='Appliance/',blank=True)
class Fashion_ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Fashion/',blank=True)
    image_2=models.ImageField(upload_to='Fashion/',blank=True)
    image_3=models.ImageField(upload_to='Fashion/',blank=True)
    image_4=models.ImageField(upload_to='Fashion/',blank=True)
class Fashion_ad3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Fashion/',blank=True)
    image_2=models.ImageField(upload_to='Fashion/',blank=True)
    image_3=models.ImageField(upload_to='Fashion/',blank=True)
class furniture_ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='furniture/',blank=True)
    image_2=models.ImageField(upload_to='furniture/',blank=True)
    image_3=models.ImageField(upload_to='furniture/',blank=True)
    image_4=models.ImageField(upload_to='furniture/',blank=True)
class furniture_ad3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='furniture/',blank=True)
    image_2=models.ImageField(upload_to='furniture/',blank=True)
    image_3=models.ImageField(upload_to='furniture/',blank=True)
class Electronics_ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Electronics/',blank=True)
    image_2=models.ImageField(upload_to='Electronics/',blank=True)
    image_3=models.ImageField(upload_to='Electronics/',blank=True)
    image_4=models.ImageField(upload_to='Electronics/',blank=True)
class Electronics_ad3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_1=models.ImageField(upload_to='Electronics/',blank=True)
    image_2=models.ImageField(upload_to='Electronics/',blank=True)
    image_3=models.ImageField(upload_to='Electronics/',blank=True)
class home_spldeal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    title=models.CharField(max_length=12)
    qutation=models.CharField(max_length=12)
class Recentsearch(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recent=models.ManyToManyField('product')
class Most_view(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    view_count=models.IntegerField(default=0)
class Most_sale(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    view_count=models.IntegerField(default=0)
class Top_Deals(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
class Festival_offer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)