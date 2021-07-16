from django.urls import path
from . import views 
from django.db import models 
from django.shortcuts import render

urlpatterns = [
    path('',views.index),
]