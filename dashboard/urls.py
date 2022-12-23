from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('add-product', views.add, name='add'),
    path('add-category', views.add_category, name='category'),
    path('search', views.api_search, name='search'),
    path('get-product/<int:product_id>', views.get_product, name='get_product'),
    path('get-product', views.get_product, name='get_product'),
    path('add-storage', views.add_storage_location, name='add_storage'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('view-products', views.view_products, name='view_products'),
    path('view-categories', views.view_categories, name='view_categories'),
    path('category/<int:category_id>', views.get_category, name='get_category'),
    path('add-project', views.add_project, name='add_project'),
    path('view-projects', views.view_projects, name='view_projects'),
    path('view-storages', views.view_storages, name='view_storages'),
]