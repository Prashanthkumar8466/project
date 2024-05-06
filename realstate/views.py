from django.shortcuts import render
from .models import employee_info
from django.contrib.auth import login,logout,authenticate
# Create your views here.
#@login_required(login_url='login')
def resume(request):
    employee=employee_info.objects.filter(user=request.user)
    return render(request,'ERP/home.html',{"employee":employee})
