from django.urls import path

from . import views 
from main.views import main_view

urlpatterns = [
    # path('digitrecognizer/',views.digitrecognizer),
    # path('',views.index,name='index'),
    # path('/login',views.login),
    path('register',views.register,name='register'),
    path('ra',views.rating),
    path('',main_view,name="main-view"),


]