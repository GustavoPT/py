from django.urls import path

from . import views 

urlpatterns = [
    path('customer/',views.customer),
    path('home/',views.home),
]