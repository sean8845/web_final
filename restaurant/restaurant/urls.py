"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from reservations import views as reservations_views
from menu import views as menu_views
from create_reservation import views as create_reservation_views


urlpatterns = [
    path('', reservations_views.home, name='home'),
    path('menu/', menu_views.menu_view, name='menu'),
    path('create_reservation/', create_reservation_views.create_reservation, name='create-reservation'),
    path('create_reservation/', create_reservation_views.reservation_success, name='reservation-success'),
    path('admin/', admin.site.urls),
]

