from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:program_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
]