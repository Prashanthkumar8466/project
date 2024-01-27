from django import forms
from .models import customer,product
from django.contrib.auth.forms import PasswordChangeForm


class customerform(forms.ModelForm):
    template_name = 'password_change.html' 
    class Meta:
        model =customer 
        fields = ['name', 'locality', 'city','phone','zipcode','state']
class productform(forms.ModelForm):
    class Meta:
        template_name = 'addproduct.html'
        model =product
        fields =['productname','price','discount','description','specifications','category','product_image']
        pass