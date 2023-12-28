from django.urls import path
from . import views 

urlpatterns = [
    path('write_review/', views.write_review, name='write_review'),
    path('review_list/', views.review_list, name='review_list'),
]
