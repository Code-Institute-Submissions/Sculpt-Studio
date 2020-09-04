from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.partners, name='partners'),
    path('add_partners/', views.add_partners, name='add_partners'),

]