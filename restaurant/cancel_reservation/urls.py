from django.urls import path
from . import views

urlpatterns = [
    path('cancel_reservation/', views.cancel_reservation, name='cancel_reservation'),  
    path('cancel_success/', views.cancel_success, name='cancel-success'),
]
