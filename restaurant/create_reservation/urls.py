from django.urls import path
from . import views

urlpatterns = [
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),

]
