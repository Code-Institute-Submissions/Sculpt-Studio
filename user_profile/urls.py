from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('user_management/<int:user_id>', views.user_management, name='user_management'),
]