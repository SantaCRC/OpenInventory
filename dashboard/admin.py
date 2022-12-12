from django.contrib import admin
from dashboard.models import Product, Category, Settings

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Settings)
