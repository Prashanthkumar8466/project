#source .venv/bin/activate
from django.db import models
from urllib import request
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from .models import Payment,cart_item, order, product,contact_u,customer
from django.views import View
from django.contrib.auth import login,logout,authenticate
from  django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import customerform,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import wishlist,mobile_ad,mobile_ad3,mobile_specification,Fashion_ad,Fashion_ad3,home_spldeal,Recentsearch
import razorpay
from .models import Top_Deals,Festival_offer,Most_view,Most_sale
# Create your views here.
def resume(request):
    return render(request,'resume_home.html')
def home(request):
    orderlst=order.objects.all()
    orderslist=home_spldeal.objects.all()
    Total=User.objects.all().count()
    active=User.objects.filter(is_active=True).count()
    Deactive=User.objects.filter(is_active=False).count()
    staff=User.objects.filter(is_staff=True).count()
    Admin=User.objects.filter(is_superuser=True).count()
    Totalorders=order.objects.all().count()
    Pendingorders=order.objects.filter(status='Pending').count()
    Deliveredorders=order.objects.filter(status='Delivered').count()
    OFDorders=order.objects.filter(status='Out For Delivery').count()
    Returnorders=order.objects.filter(status='Return').count()
    Cancelorders=order.objects.filter(status='Cancel').count()
    acceptedorders=order.objects.filter(status='Packing').count()
    amount_paid=order.objects.all()
    totalamount=sum(order.amountpaid for order in amount_paid)
    other_paid=order.objects.all()
    otheramount=sum(order.othercharges for order in other_paid)
    amount=totalamount+otheramount
    refund=order.objects.filter(status='Refund completed')
    amountrefund=sum(order.amountpaid for order in refund)
    availableamount=(totalamount+otheramount)-amountrefund
    products_by_view_count = Most_view.objects.order_by('-view_count')[:3]
    top_products = [most_view.product for most_view in products_by_view_count]
    products_by_order_count = Most_sale.objects.order_by('-view_count')[:3]
    top_orders = [most_sale.product for most_sale in products_by_order_count] 
    Products=product.objects.all()
    topdeals=Top_Deals.objects.all()
    Festival_offers=Festival_offer.objects.all()
    newproducts =product.objects .order_by('-id')[:7]
    if request.user.is_authenticated:
        recentitems,created=Recentsearch.objects.get_or_create(user=request.user)
        return render(request,'home.html',{'Festival_offers':Festival_offers,'newproducts':newproducts,'topdeals':topdeals,'Products':Products,'orders':orderslist,'Total':Total,'active':active,'Deactive':Deactive,'staff':staff,'Admin':Admin,'Totalorders':Totalorders,'Pendingorders':Pendingorders,'OFDorders':OFDorders,'Deliveredorders':Deliveredorders,'Returnorders':Returnorders,'Cancelorders':Cancelorders,'acceptedorders':acceptedorders,'amount':amount,'amountrefund':amountrefund,'otheramount':otheramount,'availableamount':availableamount,'top_products':top_products,'Products':Products,'top_orders':top_orders,'Recent':recentitems.recent.all()})
    else:
        return render(request,'home.html',{'Festival_offers':Festival_offers,'newproducts':newproducts,'topdeals':topdeals,'Products':Products,'orders':orderslist,'Total':Total,'active':active,'Deactive':Deactive,'staff':staff,'Admin':Admin,'Totalorders':Totalorders,'Pendingorders':Pendingorders,'OFDorders':OFDorders,'Deliveredorders':Deliveredorders,'Returnorders':Returnorders,'Cancelorders':Cancelorders,'acceptedorders':acceptedorders,'amount':amount,'amountrefund':amountrefund,'otheramount':otheramount,'top_orders':top_orders,'top_products':top_products,'availableamount':availableamount})
def category(request):
    products=product.objects.all()
    return render(request,"category.html",{'products':products})
def category_mobiles(request):
    Realme=product.objects.filter(Brand='Realme')
    Samsung=product.objects.filter(Brand='Samsung')
    Poco=product.objects.filter(Brand='Poco')
    Vivo=product.objects.filter(Brand='Vivo')
    Apple=product.objects.filter(Brand='Apple')
    Motorola=product.objects.filter(Brand='Motorola')
    Redmi=product.objects.filter(Brand='Redmi')
    Google=product.objects.filter(Brand='Google')
    Oppo=product.objects.filter(Brand='Oppo')
    Infinix=product.objects.filter(Brand='Infinix')
    Other=product.objects.filter(Brand='Other')
    mobile=mobile_ad.objects.all()
    mobile3=mobile_ad3.objects.all()
    return render(request,"mobiles.html",{'Realme':Realme,'Samsung':Samsung,'Poco':Poco,'Vivo':Vivo,'Apple':Apple,'Motorola':Motorola,'Redmi':Redmi,'Google':Google,'Oppo':Oppo,'Infinix':Infinix,'Other':Other,"Brand":'Realme','mobile':mobile,'mobile3':mobile3,})
def category_curd(request):
    products=product.objects.filter(category='groceries')
    return render(request,"groceries.html",{'products':products,'category':'groceries'})
def category_paneer(request):
    products=product.objects.filter(category='Furnitures')
    return render(request,"furnitures.html",{'products':products,"category":'Electronics'})
def category_cheese(request):
    products=product.objects.filter(category='Electronics')
    return render(request,"electronics.html",{'products':products,"category":'Travel'})
def category_Icecream(request):
    products=product.objects.filter(category='Beauty, Toys & More')
    return render(request,"Travel.html",{'products':products,"category":'Beauty, Toys & More'})
def product_details(request,product_id):
    products=product.objects.filter(pk=product_id)
    Product = get_object_or_404(product,pk=product_id)
    product_specifications=mobile_specification.objects.filter(pk=product_id)
    product_instance = product.objects.get(id=product_id)
    most_view_instance,created= Most_view.objects.get_or_create(product=product_instance)
    request.session['previous_url']=request.META.get('HTTP_REFERER')
    if created:
        most_view_instance.view_count = 1
    else:
        most_view_instance.view_count += 1
    most_view_instance.save()
    if request.user.is_authenticated:
        user_profile,created=Recentsearch.objects.get_or_create(user=request.user)
        user_profile.recent.add(Product)
        return render(request,"productdetails.html",{'products':products,'product_specifications':product_specifications,'product_id':product_id})
    else:
        return render(request,"productdetails.html",{'products':products,'product_specifications':product_specifications,'product_id':product_id})
    return render(request,"productdetails.html",{'products':products,'product_specifications':product_specifications,'product_id':product_id})
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
            return redirect('home')
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
        name=request.POST['name']
        locality=request.POST['locality']
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        pincode=request.POST['pincode']
        adress=customer(user_id=request.user.id,name=name,locality=locality,city=city,phone=phone,state=state,zipcode=pincode)
        adress.save()
    return render(request,"profile.html")
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
def wishlist_view(request):
    wishlistitems,created=wishlist.objects.get_or_create(user=request.user)
    return render(request,'wishlist.html',{'wishlist':wishlistitems.wish_item.all()})
@login_required(login_url='login')
def view_cart(request):
    cart_items=cart_item.objects.filter(user=request.user)
    amount=sum(item.product.price * item.quantity for item in cart_items)
    totalamount=amount+40
    if request.method=="POST":
        product_id = request.POST.get('product_id')
        new_quantity = request.POST.get('quantity')
        cart_item_instance = get_object_or_404(cart_item,pk=product_id)
        cart_item_instance.quantity = new_quantity
        cart_item_instance.update()
        return render(request,'cart.html')
    return render(request,'cart.html',{'amount':amount,'totalamount':totalamount,'cart_items':cart_items})
@login_required(login_url='login')
def add_to_cart(request,product_id):
    product_obj = product.objects.get(pk=product_id)
    if cart_item.objects.filter(user=request.user,product=product_obj).exists():
        return redirect('cart')
    else:
        cart = cart_item(user=request.user, product=product_obj)
        cart.save() 
    return redirect('cart')
def remove_from_cart(request,product_id):
    cart = cart_item(user=request.user, pk=product_id)
    cart.delete()
    return redirect('cart') 
def check_out(request):
    address=customer.objects.filter(user=request.user)
    cart_items=cart_item.objects.filter(user=request.user)
    amount=sum(item.product.price * item.quantity for item in cart_items)
    totalamount=amount+40
    return render(request,'checkout.html',locals())
'''def check_out(request):
    address=customer.objects.filter(user=request.user)
    cart_items=cart_item.objects.filter(user=request.user)
    amount=sum(item.product.price * item.quantity for item in cart_items)
    totalamount=amount+40
    razoramount=int(totalamount*100)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))
    response_payment=client.order.create(dict(amount=razoramount,currency='INR'))
    return render(request,'checkout.html',locals())'''
def order_save_online(request,product_id):
    if request.method=="POST":
        address= request.POST.get('address')
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
        cart_items = cart_item.objects.filter(user=request.user)
        if cart_items.exists():
            for cart_itm in cart_items:
                cart_itm.order= order.objects.create(user=request.user,status='pending',customer_id=1,product_id=product_id ,amountpaid=5000,othercharges=10)
                cart_itm.save() 
                cart_items.delete()
            product_instance = product.objects.get(id=product_id)
            most_sale_instance,created= Most_sale.objects.get_or_create(product=product_instance)
            if created:
                most_sale_instance.view_count = 1
            else:
                most_sale_instance.view_count += 1
            most_sale_instance.save()
            cart_items.objects.get(user=request.user).delete()  
        else:
            return redirect('checkout')
    else:
        return render(request,'ordersaved.html',locals())
def order_save(request):
    cart_items = cart_item.objects.filter(user=request.user)
    if cart_items.exists():
        for cart_itm in cart_items:
            product_id=cart_itm.product.id
            cart_itm.order= order.objects.create(user=request.user,status='pending',customer_id=1,product_id=product_id ,amountpaid=5000,othercharges=10)
            cart_itm.save() 
        cart_items.delete()
        return redirect('orders')   
    return redirect('orders')
def order_save_cod(request):
    if request.method=="POST":
        address= request.POST.get('address')
    cart_items = cart_item.objects.filter(user=request.user)
    if cart_items.exists():
        for cart_itm in cart_items:
            product_id=cart_itm.product.id
            cart_itm.order= order.objects.create(user=request.user,status='pending',customer=address,product_id=product_id ,amountpaid=5000,othercharges=10)
            cart_itm.save() 
        cart_items.delete()
        product_instance = product.objects.get(id=product_id)
        most_sale_instance,created= Most_sale.objects.get_or_create(product=product_instance)
        if created:
            most_sale_instance.view_count = 1
        else:
            most_sale_instance.view_count += 1
        most_sale_instance.save()
        return redirect('orders') 
    return render(request,'checkout.html',{'totalamount':totalamount})
@login_required(login_url='login')
def order_view(request):
    orderslist=order.objects.filter(user=request.user)
    return render(request,'orders.html',{'orders':orderslist})
# adding products page functions
#product adding 
@login_required(login_url='login')
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
#fashion adding 
@login_required(login_url='login')
def add_fashion(request):
    return render(request,'addfashion.html')
def view_last_fashion(request):
    products=product.objects.filter(category='Fashion').order_by('-id')[:3]
    return render(request,'addfashion.html',{'products':products})
def category_fashion(request):
    mobile=Fashion_ad.objects.all()
    mobile3=Fashion_ad3.objects.all()
    products=product.objects.filter(category='Fashion')
    return render(request,"fashion.html",{'products':products,"category":'Fashion','mobile':mobile,'mobile3':mobile3}) 
#mobile adding
@login_required(login_url='login')
def add_Mobile(request):
    if request.method=="POST":
            productname=request.POST['productname']
            price=request.POST['price']
            discount=request.POST['discount']
            description=request.POST['description']
            category=request.POST['category']
            product_image=request.FILES.get('product_image')
            Brand=request.POST['Brand']
            Product=product.objects.create(productname=productname,price=price,discount=discount,description=description,category=category,product_image=product_image ,Brand=Brand,user=request.user)
            products=product.objects.filter(user=request.user).order_by('-id')[:1]
            In_the_Box=request.POST['In_the_Box']
            Model_Number=request.POST['Model_Number']
            mobile_specification.objects.create(In_the_Box= In_the_Box,Model_Number=Model_Number,user=request.user,product=Product)
    return render(request,'mobileadd.html')
def viewall_Mobile(request,brand_name):
    wishlistitems,created=wishlist.objects.get_or_create(user=request.user)
    products = product.objects.filter(Brand=brand_name)
    return render(request,'mobilesview.html',{'Realme':products,'brand_name': brand_name},{'wishlist':wishlistitems.wish_item.all()})
def view_last_add(request):
    products=product.objects.filter(category='Mobiles').order_by('-id')[:3]
    return render(request,'mobileadd.html',{'products':products})
#end add product functions 
#appliances
@login_required(login_url='login')
def add_appliances(request):
    return render(request,'addappliances.html')
def view_appliances(request):
    return render(request,'appliances.html')
def view_all_appliances(request,brand_name):
    products = product.objects.filter(sub_category=brand_name)
    return render(request,'mobilesview.html',{'Realme':products,'brand_name': brand_name})
@login_required(login_url='login')
def allorder_view(request):
    orderslist,created=order.objects.get_or_create(user=request.user)
    return render(request,'orders.html',{'orders':orderslist.product.all()})
@login_required(login_url='login')
def order_details(request,pk):
    order_details=order.objects.filter(user=request.user,id=pk)
    return render(request,'orderdetails.html',{'orders':order_details,'pk':pk})
def all_categories(request):
    return render(request,'allcategories.html')
def back_view(request):
    previous_url=request.session.get('previous_url','/')
    return redirect(previous_url)
 # Redirect to the home page if no previous URL is found
def add_to_history(request):
    history = request.session.get('history', [])
    current_url = request.build_absolute_uri()
    if current_url not in history:
        history.append(current_url)
        request.session['history'] = history
def get_previous_url(request):
    history = request.session.get('history', [])
    if len(history) >= 2:
        # Pop the current URL from history
        history.pop()
        # Return the previous URL
        return history.pop()
    return None
def Error_page(request, exception):
    return render(request, "404.html", {}, status=404)