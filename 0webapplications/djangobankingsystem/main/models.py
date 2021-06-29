from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 

class Seller(models.Model):
    id = models.Field(primary_key=True)
    name = models.CharField(max_length=10)

class Product(models.Model):
    # product_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=4,decimal_places=4,null=True)
    name = models.CharField(max_length=10)
    isService = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

class Card(models.Model):
    number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    backcode = models.IntegerField()
    image = models.ImageField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Transaction(models.Model):
    id = models.Field(primary_key=True)
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=4,decimal_places=4,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Account(models.Model):
    id = models.Field(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=4,decimal_places=4,null=True)

    

 