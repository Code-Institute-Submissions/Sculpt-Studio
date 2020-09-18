from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('user_selection/', views.user_selection, name='user_selection'),
    path('user_management/<int:user_id>', views.user_management, name='user_management'),
    path('book_meeting/<int:user_id>', views.book_meeting, name='book_meeting'),
]