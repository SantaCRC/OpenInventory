from django.contrib import admin
from dashboard.models import Product, Category, Settings, Storage, Project

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Settings)
admin.site.register(Storage)
admin.site.register(Project)
