from django.contrib import admin
from . models  import contact_u,role,employee_info
# Register your models here.
@admin.register(contact_u)
class contactModelAdmin(admin.ModelAdmin):
    list_display=["id","name","phone","email"]
@admin.register(role)
class roleModelAdmin(admin.ModelAdmin):
    list_display=["id","role_name"]
@admin.register(employee_info)
class employee_infoModelAdmin(admin.ModelAdmin):
    list_display=["id","name"]