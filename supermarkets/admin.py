from django.contrib import admin
from . models  import Payment, cart_item, order,product,contact_u,customer,wishlist,mobile_ad,mobile_ad3,mobile_specification
from . models  import furniture_ad,furniture_ad3,Appliance_ad,Appliance_ad3,Fashion_ad,Fashion_ad3,Electronics_ad,Electronics_ad3,home_spldeal
# Register your models here.
@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display=["id","productname","category","discount","product_image"]
#mobile-related models
@admin.register(mobile_specification)
class mobile_specificationModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(mobile_ad)
class mobileadModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(mobile_ad3)
class mobilead3ModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
#end mobile-related models
#furniture
@admin.register(furniture_ad)
class furniture_adModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(furniture_ad3)
class furniture_ad3ModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
#electonics
@admin.register(Electronics_ad)
class Electronics_adModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(Electronics_ad3)
class Electronics_ad3ModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
#appliances
@admin.register(Appliance_ad)
class Appliance_adModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(Appliance_ad3)
class Appliance_ad3ModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
#fashion
@admin.register(Fashion_ad)
class Fashion_adModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
@admin.register(Fashion_ad3)
class Fashion_ad3ModelAdmin(admin.ModelAdmin):
    list_display=["id","user"]
#home_slad
@admin.register(home_spldeal)
class home_spldealModelAdmin(admin.ModelAdmin):
    list_display=["id","title"]
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
