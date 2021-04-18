from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# users 
# 
# category 


class Product(models.Model):
    title = models.CharField
    price = models.DecimalField
    discount_price = models.DecimalField
    description = models.TextField


 

class Item(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500)
    def __str__(self):
        return self.name
# class Ticket(models.Model):
#     ticket_name = models.CharField
#     ticket_number 
#     ticket_price 
#     ticket_
    
#     def __str__(self):
#         return self.name

