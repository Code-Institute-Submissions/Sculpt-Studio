from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('delete_testimonials/<int:testimonial_id>', views.delete_testimonials, name='delete_testimonials'),
]