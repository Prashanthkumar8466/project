from django import forms
from .models import customer
from django.contrib.auth.forms import PasswordChangeForm


class customerform(forms.ModelForm):
    template_name = 'password_change.html' 
    class Meta:
        model =customer 
        fields = ['name', 'locality', 'city','phone','zipcode','state']
