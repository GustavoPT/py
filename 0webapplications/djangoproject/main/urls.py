from django.urls import path
from . import views 
from django.db import models 
from django.shortcuts import render

def order(request):
    return render(request, "or.html",{})

urlpatterns = [
    path('digitrecognizer/',views.digitrecognizer),
    path('searchengine',views.searchengine),
    path('bi/',views.bitcoin),
]