from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.programs, name='programs'),
    path('<int:program_id>', views.program_details, name='program_details'),
    path('edit_program/<int:program_id>', views.edit_program, name='edit_program'),
    path('delete_program/<int:program_id>', views.delete_program, name='delete_program'),
    path('add_program/', views.add_program, name='add_program'),
]