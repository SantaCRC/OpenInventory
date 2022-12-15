from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('add', views.add, name='add'),
    path('add-category', views.add_category, name='category'),
    path('search', views.api_search, name='search'),
    path('get-product/<int:product_id>', views.get_product, name='get_product'),
    path('get-product', views.get_product, name='get_product'),
    path('add-storage', views.add_storage_location, name='add_storage'),
]