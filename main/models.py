from django.db import models
from django.contrib.auth.models import AbstractUser, User




# Create your models here.
class Closes(models.Model):
    nom = models.CharField(max_length=255, blank=True, default='name')
    price = models.FloatField(blank=True, default='',)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.nom

class AllUser(models.Model):
    user_name = models.CharField(max_length=255, default='')
    user_lastname = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')
    virifed = models.CharField(max_length=255, blank=True, default='0')
    caches = models.TextField(default='{}')
    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,  on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class shop(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.client.username

class shopitem(models.Model):
    sho = models.ForeignKey(shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.sho) + ' ' +self.product.name

    class Meta:
        verbose_name_plural = '2. Shop Item'

