from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.purchase_checkout, name='purchase_checkout'),
    path('purchase_successful/<order_number>', views.purchase_successful, name='purchase_successful'),
    path('user_purchases/<int:user_id>', views.user_purchases, name='user_purchases'),
]