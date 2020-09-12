from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.purchase_checkout, name='purchase_checkout'),
    path('purchase_successful/', views.purchase_successful, name='purchase_successful'),
]