
from urllib import request
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from .models import Payment, cart_item, order, product,contact_u,customer
from django.views import View
from django.contrib.auth import login,logout,authenticate
from  django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import customerform,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import wishlist
import razorpay
# Create your views here.
def home(request):
    return render(request,"home.html")
'''class category(View):
    def get(self,request,val):
        products=product.objects.get(category=val)
        return render(request,'category.html',{"products":products},locals())'''
def category(request):
    products=product.objects.all()
    return render(request,"category.html",{'products':products})
def category_milk(request):
    products=product.objects.filter(category='Milk')
    return render(request,"category.html",{'products':products,'category':'milk'})
def category_curd(request):
    products=product.objects.filter(category='Curd')
    return render(request,"category.html",{'products':products,'category':'curd'})
def category_kulfi(request):
    products=product.objects.filter(category='kl')
    return render(request,"category.html",{'products':products,"category":'kulfi'})
def category_paneer(request):
    products=product.objects.filter(category='pa')
    return render(request,"category.html",{'products':products,"category":'paneer'})
def category_ghee(request):
    products=product.objects.filter(category='gh')
    return render(request,"category.html",{'products':products,"category":'ghee'})
def category_cheese(request):
    products=product.objects.filter(category='ch')
    return render(request,"category.html",{'products':products,"category":'cheese'})

def category_Icecream(request):
    products=product.objects.filter(category='Ice-Cream')
    return render(request,"category.html",{'products':products,"category":'Ice-Cream'})

def product_details(request,product_id):
    products=product.objects.filter(pk=product_id)
    return render(request,"productdetails.html",{'products':products})
def about(request):
    return render(request,"about.html")
def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact=contact_u(name=name,email=email,phone=phone,message=message)
        contact.save()
        message='saved your message'
        return render(request,'contact.html',{'message':message})
    else:
        return render(request,"contact.html")
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            error_message = 'invalid username or password'
            return render(request,'login.html',{'error_message':error_message})
    else:
        return render(request,"login.html")
def logout_view(request):
    logout(request)
    return redirect('login')
def signup_view(request):
    if request.method=="POST":
        First_name=request.POST['Firstname']
        Last_name=request.POST['Lastname']
        username=request.POST['username']
        email=request.POST['email']
        p1=request.POST['password']
        p2=request.POST['confirm_password']
        if User.objects.filter(email=email).exists():
            message='email already exist'
            return render(request,'signup.html',{'message':message})
        elif (p1==p2):
            user=User.objects.create_user(username=username,email=email,password=p1)
            user.first_name=First_name
            user.last_name=Last_name
            user.save()
            return redirect('login')
        else:
            message='Enter same password'
            return render(request,'signup.html',{"message":message})
    else:
        return render(request,"signup.html")

@login_required(login_url='login')
def profile_view(request):
    if request.method=='POST':
        form=customerform(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
        else:
            form=customerform()
            message='enter vaild details'
            return render(request,'profile.html',{'message':message,'form':form})
    else:
        form=customerform()
        return render(request,"profile.html",{'form':form})
@login_required(login_url='login')
def address_view(request):
    address=customer.objects.filter(user=request.user)
    return render(request,"address.html",{'address':address})
def address_delete(request,address_id):
    address=customer.objects.get(pk=address_id)
    address.delete()
    return render(request,'address.html')
@login_required(login_url='login')
def updateaddress(request,pk):
    update_profile=customer.objects.get(user=request.user,id=pk)
    if request.method=='POST':
        form=customerform(request.POST,instance=update_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('address')
        else:
            form=customerform()
            message='enter vaild details'
            return render(request,'updateaddress.html',{'message':message,'form':form})
    else:
        form=customerform(instance=update_profile)
        return render(request,"updateaddress.html",{'form':form})
def password_change_done(request):
    return render(request, 'passwordchangedone.html') 
def password_reset_confirm(request):
    message='sucessfully sent a link to your email address in email you can your password from the link'
    return render(request,'login.html',{'message':message})
@login_required(login_url='login')
def add_to_wishlist(request, product_id):
    Product = get_object_or_404(product,pk=product_id)
    user_profile,created = wishlist.objects.get_or_create(user=request.user)
    user_profile.wish_item.add(Product)
    return redirect('wishlist')
def remove_from_wishlist(request, product_id):
    Product = get_object_or_404(product,pk=product_id)
    user_profile,created = wishlist.objects.get_or_create(user=request.user)
    user_profile.wish_item.remove(Product)
    return redirect('wishlist')
@login_required(login_url='login')  
def wishlist_view(request,):
    wishlistitems,created=wishlist.objects.get_or_create(user=request.user)
    return render(request,'wishlist.html',{'wishlist':wishlistitems.wish_item.all()})
@login_required(login_url='login')
def view_cart(request):
    cart=cart_item.objects.first()
    cart_items=cart.cart_items.all()
    amount=sum(product.discount for product in cart_items)
    totalamount=amount+40
    return render(request,'cart.html',{'amount':amount,'totalamount':totalamount,'cart_items':cart_items})
@login_required(login_url='login')
def add_to_cart(request,product_id):
    Product=get_object_or_404(product,pk=product_id)
    cart_items,created=cart_item.objects.get_or_create(user=request.user)
    cart_items.cart_items.add( Product)
    return redirect('cart')
def remove_from_cart(request,product_id):
    Product=get_object_or_404(product,pk=product_id)
    cart_items,created=cart_item.objects.get_or_create(user=request.user)
    cart_items.cart_items.remove(Product)
    return redirect('cart')
def check_out(request):
    address=customer.objects.filter(user=request.user)
    cart=cart_item.objects.first()
    cart_items=cart.cart_items.all()
    amount=sum(product.discount for product in cart_items)
    totalamount=amount+40
    razoramount=int(totalamount*100)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))
    response_payment=client.order.create(dict(amount=razoramount,currency='INR'))
    order_id=response_payment['id']
    order_status=response_payment['status']
    custom=customer.objects.get(id=1)
    return render(request,'checkout.html',locals())
def order_save(request):
    if request.method=="POST":
        if order_status=='created': 
            payment=Payment(
            user=request.user,
            amount=razoramount,
            razorpay_order_id=order_id,
            razorpay_payment_status=order_status,
            paid=True,
        )
        payment.save() 
        address=customer.objects.filter(user=request.user)
        cart=cart_item.objects.first()
        cart_items=cart.cart_items.all()
        amount=sum(product.discount for product in cart_items)
        totalamount=amount+40
        razoramount=int(totalamount*100)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))
        response_payment=client.order.create(dict(amount=razoramount,currency='INR'))
        order_id=response_payment['id']
        order_status=response_payment['status']
        custom=customer.objects.get(id=1)
        for product in cart_items:
            orders=order.objects.create(
                user=request.user,
                product=product,
                customer= custom,
            )
            orders.save()  
        else:
            return redirect('checkout')
    else:
        return render(request,'ordersaved.html',locals())  
def order_view(request):
    orderslist=order.objects.prefetch_related('orderitem_set__product').all()
    return render(request,'orders.html',{'orders':orderslist})
#product adding 
def add_product(request):
    if request.method=="POST":
            productname=request.POST['productname']
            price=request.POST['price']
            discount=request.POST['discount']
            specifications=request.POST['specifications']
            description=request.POST['description']
            product_image=request.FILES.get('product_image')
            category=request.POST['category']
            add_prdt=product(productname=productname,price=price,discount=discount,specifications=specifications,description=description,product_image=product_image ,category=category)
            add_prdt.save()
            return redirect('addproduct')
    return render(request,'addproduct.html')
        