from django.contrib import admin
from . models  import Payment, cart_item, order,product,contact_u,customer,wishlist
# Register your models here.
@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display=["id","productname","category","discount","product_image"]
@admin.register(contact_u)
class contactModelAdmin(admin.ModelAdmin):
    list_display=["id","name","phone","email"]
@admin.register(customer)
class contactModelAdmin(admin.ModelAdmin):
    list_display=["id","user","name","state","zipcode",'phone']
@admin.register(wishlist)
class wishlistModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(cart_item)
class cartitemsModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(order)
class orderplacedModelAdmin(admin.ModelAdmin):
   list_display=['id']
admin.site.register(Payment)