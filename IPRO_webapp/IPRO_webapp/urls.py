"""IPRO_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from seller import views as seller_views
from catalogue import views as catalogue_views
from Messaging_System import views as messaging_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/profile/', user_views.userAcct, name='account'),
    path('accounts/home/', seller_views.sellInterface, name='seller'),
    path('upload/', seller_views.uploadText, name='uploadtext'),
    path('catalogue/', catalogue_views.catalogueInterface, name='catalogue'),
    path('browse/', catalogue_views.browseTextbooks, name='browse'),
    path('search/', catalogue_views.searchCatalogue, name='search'),
    path('wishlistform/', catalogue_views.wishlistForm, name='wishlistform'),
    path('wishlist/', user_views.wishlist, name='wishlist'),
    path('reportfraud/', user_views.reportFraud, name='repfraud'),
    path('Messages', messaging_views.showChats, name='Messages'),
    path('Messages/newchat', messaging_views.newChat, name='newchat'),
    path('Messages/<int:pk>/', messaging_views.showMessages, name='chat'),
    path('Messages/<int:pk>/NewMessage/', messaging_views.newMessage, name='NewMessage'),
    
]

