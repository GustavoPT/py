from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=30,decimal_places=3)
    discount_price = models.DecimalField(max_digits=30,decimal_places=3)
    category = models.CharField(max_length=300)
    description = models.TextField()
    image = models.CharField(max_length=300)