from django.urls import path

from . import views 

urlpatterns = [
    path('digitrecognizer/',views.digitrecognizer),
    path('search/',views.search),
]