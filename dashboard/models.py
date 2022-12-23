from django.db import models

# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

# Category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
    
# Settings model
class Settings(models.Model):
    conf_currency = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Settings"
        verbose_name = "Setting"

# Storage model
class Storage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200)
    parent_storage = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Storages"
        verbose_name = "Storage"

# Project model
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    list_products = models.ManyToManyField(Product, blank=True) 

    def __str__(self):
        return self.name
