from django.urls import path
from .import views
urlpatterns = [
    path('ERP-Realstate', views.resume,name="ERP-Realstate"),
]