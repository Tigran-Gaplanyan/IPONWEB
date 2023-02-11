from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="StorageCategory/", blank=True, null =True)


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="ItemCategory/", blank=True, null=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="Customer/", blank=True, null=True)
    registered_at = models.DateTimeField(default=timezone.now)


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="StoreOwner/", blank=True, null=True)
    registered_at = models.DateTimeField(default=timezone.now)


class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="Item/", blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    info = models.CharField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.PositiveIntegerField(default=0)


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)


