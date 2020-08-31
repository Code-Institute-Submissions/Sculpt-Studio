from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('add_testimonials/', views.add_testimonials, name='add_testimonials'),
]