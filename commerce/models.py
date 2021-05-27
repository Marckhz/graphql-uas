from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):

    def __str__(self):
        return self.username


class Shop(models.Model):

    shop_name = models.CharField(max_length=50, null=False)
    description =  models.TextField(null=False)
    is_active = models.BooleanField(null=False)
    image = models.URLField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.shop_name

#a shop can have multiple menus

class ShopMenu(models.Model):

    genre = models.CharField(max_length=50, null=False)
    creation_date = models.DateField(auto_now=True)
    image = models.ImageField(null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.genre

class MenuItems(models.Model):
    
    item = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    creation_date = models.DateField(auto_now=False)
    menu = models.ForeignKey(ShopMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Service(models.Model):

    service = models.TextField()
    

class Product(models.Model):
    
    product = models.TextField(null=False)
    def __str__(self):
        return self.product

class Reviews(models.Model):

    score = models.IntegerField(null=True)
    summary = models.TextField(null=True)
    text = models.TextField(null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)