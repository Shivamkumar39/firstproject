from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('about', views.about, name = 'about'),
    path('products', views.products, name = 'products'),
    path('contact', views.contact, name = 'contact'),
    
]