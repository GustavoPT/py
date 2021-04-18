from django.urls import path

from . import views 

urlpatterns = [
    # path('digitrecognizer/',views.digitrecognizer),
    path('',views.index,name='index'),
    # path('/login',views.login),
    path('register',views.register,name='register'),

]