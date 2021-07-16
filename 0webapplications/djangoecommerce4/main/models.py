from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser
# python3 manage.py makemigrations
# python3 manage.py migrate


class User(AbstractUser):
    pass 

class Seller(models.Model):
    id = models.Field(primary_key=True)
    name = models.CharField(max_length=10)

    # product_id = models.AutoField(primary_key=True)

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


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=30,decimal_places=3)
    discount_price = models.DecimalField(max_digits=30,decimal_places=3)
    category = models.CharField(max_length=300)
    description = models.TextField()
    image = models.CharField(max_length=300)
    isService = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

class Cart(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE)

class Rating(models.Model):
    image = models.ImageField(upload_to='images/')
    score = models.IntegerField(default=0,validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])

    def __str__(self):
        return str(self.pk)

# create my own rating system 
# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         return self.title

# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#     publications = models.ManyToManyField(Publication)

#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ['headline']
