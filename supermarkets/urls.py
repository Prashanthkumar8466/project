from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import add_to_cart,password_change_done, remove_from_wishlist, view_cart
from .views import add_to_wishlist
urlpatterns = [
    path('home', views.home,name="home"),
    #products 
    path('categories/', views.all_categories,name="categories"),
    path('category/', views.category,name="category"),
    path('Groceries', views.category_curd,name="Groceries"),
    path('Mobiles', views.category_mobiles,name="Mobiles"),
    path('Fashion', views.category_fashion,name="Fashion"),
    path('Electronics', views.category_cheese,name="Electronics"),
    path('Home & Furnitures', views.category_paneer,name="Home & Furnitures"),
    path('Appliances', views.category_ghee,name="Appliances"),
    path('Travel', views.category_Icecream,name="Travel"),
    path('productdetails/<int:product_id>/', views.product_details,name="productdetails_product_id"),
    path('about', views.about,name="about"),
    path('contactus', views.contactus,name="contactus"),
    #login/sign func
    path('login', views.login_view,name="login"),
    path('logout', views.logout_view,name="logout"),
    path('signup', views.signup_view,name="signup"),
    #profile
    path('profile', views.profile_view,name="profile"),
    path('address', views.address_view,name="address"),
    path('address/<int:address_id>/', views.address_delete,name="address"),
    path('address/<int:pk>', views.updateaddress,name="address_int_pk"), 
    #password 
    path('password_change',auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change_done/', password_change_done, name='password_change_done'),
    path('password_Reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #wishlist function
    path('add-to-wishlist/<int:product_id>/',add_to_wishlist,name='add-to-wishlist'),
    path('remove-from-wishlist/<int:product_id>/',remove_from_wishlist,name='remove-from-wishlist'),
    path('wishlist',views.wishlist_view ,name='wishlist'),
    #card functions
    path('cart',view_cart,name='cart'),
    path('add-to-cart/<int:product_id>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/',views.remove_from_cart,name='remove-from-cart'),
    path('checkout',views.check_out,name='checkout'),
    #orders
    path('orders',views.order_view,name='orders'),
    path('ordersave',views.order_save,name='ordersave'),
    path('orderdetails/<int:pk>/', views.order_details, name='orderdetails'),
    #admin/staff
    path('addproduct',views.add_product,name='addproduct'),
    path('allorders',views.allorder_view,name='allorders'),
    ]