from django.shortcuts import render,redirect
from .models import employee_info
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required(login_url='login')
def company_creation(request):
    employee=employee_info.objects.filter(user=request.user)
    return render(request,'ERP/company_creation.html',{"employee":employee})
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            employee=employee_info.objects.filter(user=request.user)
            return redirect("ERP-Realestate")
        else:
            error_message = 'invalid username or password'
            return render(request,'ERP/login.html',{'error_message':error_message})
    else:
        return render(request,"ERP/login.html")
@login_required(login_url='ERP-login')
def resume(request):
    employee=employee_info.objects.filter(user=request.user)
    return render(request,'ERP/home.html',{"employee":employee})