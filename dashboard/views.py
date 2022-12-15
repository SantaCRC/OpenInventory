from django.shortcuts import render, redirect, HttpResponse
from dashboard.models import Product, Category, Storage
from dashboard.forms import ProductForm, CategoryForm, StorageForm
from django.contrib import messages
from dynamic_preferences.registries import global_preferences_registry
import json

# We instantiate a manager for our global preferences
global_preferences = global_preferences_registry.manager()

def index(request):
  return render(request, 'dashboard.html', {"title": "Buscar Producto"})

def settings(request):
  return render(request, 'settings.html', {"title": "Configuración"})

def add(request):
  if request.method == "POST":
    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid():
      product_form.save()
      messages.success(request, "Producto agregado correctamente")
    else:
      messages.error(request, "Error al agregar el producto")
      messages.error(request, product_form.errors)
    
    return redirect('dashboard:add')
  else:
    product_form = ProductForm()
    products = Product.objects.all()
    categories = Category.objects.all()
    locations = Storage.objects.all()
  return render(request, 'add.html', {"title": "Agregar Producto", "product_form": product_form, "products": products, "categories": categories, "locations": locations})

def add_category(request):
  if request.method == "POST":
    category_form = CategoryForm(request.POST)
    if category_form.is_valid():
      category_form.save()
      messages.success(request, "Categoría agregada correctamente")
    else:
      messages.error(request, "Error al agregar la categoría")
      messages.error(request, category_form.errors)
    return redirect('dashboard:category')
  else:
    category_form = CategoryForm()
  
  return render(request, 'add-category.html', {"title": "Agregar Categoría"})

#Search product
def search(request):
  if request.method == "GET":
    product_name = request.GET.get('product_name')
    products = Product.objects.filter(name__icontains=product_name)
    return render(request, 'search.html', {"title": "Buscar Producto", "products": products})
  else:
    pass
  
  return

# Product page
def get_product(request, product_id):
  currency = global_preferences['general__currency_symbol']
  product = Product.objects.get(id=product_id)
  category = Category.objects.get(id=product.category)
  categories = Category.objects.all()
  location = Storage.objects.get(id=product.location)
  
  if request.method == "POST":
    product_id = request.POST.get('id')
    product = Product.objects.get(id=product_id)
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      messages.success(request, "Producto actualizado correctamente")
      return redirect(request.META.get('HTTP_REFERER'))
    else:
      messages.error(request, "Error al actualizar el producto")
      messages.error(request, form.errors)
      return redirect(request.META.get('HTTP_REFERER'))
  else:
    pass
  
  return render(request, 'product.html', {"title": "Producto", "product": product, "category": category, "currency": currency, "categories": categories, "location": location})

def settings(request):
  if request.method == "POST":
    pass
  
  return render(request, 'settings.html', {"title": "Configuración"})

# Api search
def api_search(request):
  if request.method == "GET":
    term = request.GET.get('term')
    data = []
    if term:
        items = Product.objects.filter(name__icontains=term).values('id','name')
        serialized_data = list(items)
        data = json.dumps(serialized_data)

    return HttpResponse(data, content_type='application/json')

# add storage location
def add_storage_location(request):
  if request.method == "POST":
    storage_form = StorageForm(request.POST)
    if storage_form.is_valid():
      storage_form.save()
      messages.success(request, "Ubicación agregada correctamente")
    else:
      messages.error(request, "Error al agregar la ubicación")
      messages.error(request, storage_form.errors)
    return redirect('dashboard:add_storage')
  else:
    storage_form = StorageForm()
    storages = Storage.objects.all()
  return render(request, 'add-storage.html', {"title": "Agregar Ubicación", "storage_form": storage_form, "storages": storages})