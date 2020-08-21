from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.programs, name='programs'),
    path('programs/<int:program_id>', views.program_details, name='program_details'),
]