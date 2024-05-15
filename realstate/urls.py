from django.urls import path
from .import views
urlpatterns = [
    path('ERP-Realestate', views.resume,name="ERP-Realestate"),
    path('ERP-login', views.login_view,name="ERP-login"),
    path('company_creation', views.company_creation,name="company_creation"),
]