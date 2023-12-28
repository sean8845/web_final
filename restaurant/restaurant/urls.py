from django.contrib import admin
from django.urls import path, include
from reservations import views as reservations_views
from menu import views as menu_views
from create_reservation import views as create_reservation_views
from cancel_reservation.views import cancel_reservation
from table_info.views import reservation_list
from review.views import write_review, review_list

urlpatterns = [
    path('', reservations_views.home, name='home'),
    path('menu/', menu_views.menu_view, name='menu'),
    path('create_reservation/', create_reservation_views.create_reservation, name='create-reservation'),
    path('reservation_success/', create_reservation_views.reservation_success, name='reservation-success'),
    path('cancel_reservation/', include('cancel_reservation.urls')),    
    path('table_info/', reservation_list, name='table_info'), 
    path('write_review/', write_review, name='write_review'),
    path('review_list/', review_list, name='review_list'),
    path('admin/', admin.site.urls),
]