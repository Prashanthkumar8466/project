
from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
CATEGORY_CHOICES = [
    ('Ml', 'Milk'),
    ('cu', 'Curd'),
    ('la', 'lassi'),
    ('gh', 'ghee'),
    ('pa', 'paneer'),
    ('ch', 'cheese'),
    ('Ic','Ice-Cream'),
    ('kl','kulfi')
]
STATE_CHOICE=[
    ('andhraPradesh','andhraPradesh'),
    ('Telengana','Telengana'),
    ('chennai','chennai'),
    ('thamilNadu','thamilNadu'),
    ('Delhi','Delhi'),
    ('madhyaPradesh','madhyaPradesh'),
]
STATUS_CHOICE=[
    ('pending','pending'),
    ('on the way','on the way'),
    ('cancel','cancel'),
    ('deliverd','deliverd'),
]
class product(models.Model):
    productname=models.TextField(max_length=100)
    price=models.FloatField()
    discount=models.FloatField(default=0)
    description=models.TextField()
    specifications=models.TextField(default="")
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES, default='Ml')
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.productname
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
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    zipcode=models.DecimalField(max_digits=6,decimal_places=0)
    state=models.TextField(choices=STATE_CHOICE, default='Telangana')
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
    customer=models.ManyToManyField(customer)
    product=models.ManyToManyField(product)
    quality=models.PositiveSmallIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')
    #payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    