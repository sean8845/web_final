from django.urls import path
from . import views

urlpatterns = [
    path('table_info/', views.table_info, name='table_info'),
    
]