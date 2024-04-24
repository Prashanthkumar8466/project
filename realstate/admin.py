from django.contrib import admin
from . models  import contact_u
# Register your models here.
@admin.register(contact_u)
class contactModelAdmin(admin.ModelAdmin):
    list_display=["id","name","phone","email"]