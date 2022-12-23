from django.shortcuts import render, redirect, HttpResponse
from dashboard.models import Product, Category, Storage, Project
from dashboard.forms import ProductForm, CategoryForm, StorageForm, ProjectForm
from django.contrib import messages
from dynamic_preferences.registries import global_preferences_registry
import json

# We instantiate a manager for our global preferences
global_preferences = global_preferences_registry.manager()

#get index page
def index(request):
  return render(request, 'dashboard.html', {"title": "Buscar Producto"})

# get settings page
def settings(request):
  return render(request, 'settings.html', {"title": "Configuración"})

# Add product to inventory
def add(request):
  if request.method == "POST":
    error_message = ""
    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid():
      product_form.save()
      messages.success(request, "Producto agregado correctamente")
      message = 'ok'
    else:
      messages.error(request, "Error al agregar el producto")
      messages.error(request, product_form.errors)
      message = 'error'
      error_message = product_form.errors

    product_form = ProductForm()
    products = Product.objects.all()
    categories = Category.objects.all()
    locations = Storage.objects.all()
    
    return render(request, 'add-product.html', {"title": "Agregar Producto", "product_form": product_form, "products": products, "categories": categories, "locations": locations, "message": message, "error_message": error_message})
  else:
    product_form = ProductForm()
    products = Product.objects.all()
    categories = Category.objects.all()
    locations = Storage.objects.all()
  return render(request, 'add-product.html', {"title": "Agregar Producto", "product_form": product_form, "products": products, "categories": categories, "locations": locations})

# add category
def add_category(request):
  categories = Category.objects.all()
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
  
  return render(request, 'add-category.html', {"title": "Agregar Categoría","categories": categories})

#Search product
def search(request):
  if request.method == "GET":
    product_name = request.GET.get('product_name')
    products = Product.objects.filter(name__icontains=product_name)
    return render(request, 'search.html', {"title": "Buscar Producto", "products": products})
  else:
    pass
  
  return

# Product page and options (edit, delete, add stock, delete stock)
def get_product(request, product_id):
  currency = global_preferences['general__currency_symbol']
  product = Product.objects.get(id=product_id)
  category = Category.objects.get(id=product.category)
  categories = Category.objects.all()
  location = Storage.objects.get(id=product.location)
  locations = Storage.objects.all()
  
  if request.method == "POST":
    product = Product.objects.get(id=product_id)
    form = ProductForm(request.POST, request.FILES, instance=product)
    option = request.POST.get('option')
    
    if option == "add":
      stock = request.POST.get('stock')
      product.stock = product.stock + int(stock)
      product.save()
      messages.success(request, "Stock actualizado correctamente")
      return redirect(request.META.get('HTTP_REFERER'))
    
    elif option == "delete":
      stock = request.POST.get('stock')
      if product.stock == 0:
        messages.error(request, "No hay stock para eliminar")
        return redirect(request.META.get('HTTP_REFERER'))
      if product.stock < int(stock):
        messages.error(request, "No hay suficiente stock para eliminar")
        return redirect(request.META.get('HTTP_REFERER'))
      product.stock = product.stock - int(stock)
      product.save()
      messages.success(request, "Stock actualizado correctamente")
      return redirect(request.META.get('HTTP_REFERER'))
    
    elif option == "delete_product":
      product.delete()
      messages.success(request, "Producto eliminado correctamente")
      return redirect("dashboard:index")
    
    else:
      
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
  
  return render(request, 'product.html', {"title": "Producto", "product": product, "category": category, "currency": currency, "categories": categories, "location": location, "locations": locations})

# get settings page
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
        items = Product.objects.filter(name__icontains=term).values('id','name', 'price', 'category', 'location', 'image', 'description')
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

# view list of products
def view_products(request):
  products = Product.objects.all()
  locations = Storage.objects.all()
  locations = list(locations)
  categories = Category.objects.all()
  currency = global_preferences['general__currency_symbol']
  return render(request, 'view-products.html', {"title": "Productos", "products": products, "locations": locations, "currency": currency, "categories": categories }) 

# view list of categories
def view_categories(request):
  categories = Category.objects.all()
  return render(request, 'view-categories.html', {"title": "Categorías", "categories": categories})

# get category
def get_category(request, category_id):
  if request.method == "POST":
    category = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST, instance=category)
    option = request.POST.get('option')
    
    if option == "delete_category":
      category.delete()
      messages.success(request, "Categoría eliminada correctamente")
      return redirect("dashboard:view_categories")
    
    if form.is_valid():
      form.save()
      messages.success(request, "Categoría actualizada correctamente")
      return redirect(request.META.get('HTTP_REFERER'))
    
  category = Category.objects.get(id=category_id)
  return render(request, 'category.html', {"title": "Categoría", "category": category}) 

# add project
def add_project(request):
  if request.method == "POST":
    project_form = ProjectForm(request.POST)
    if project_form.is_valid():
      project_form.save()
      messages.success(request, "Proyecto agregado correctamente")
    else:
      messages.error(request, "Error al agregar el proyecto")
      messages.error(request, project_form.errors)
    return redirect('dashboard:add_project')
  else:
    project_form = ProjectForm()
    projects = Project.objects.all()
  return render(request, 'add-project.html', {"title": "Agregar Proyecto", "project_form": project_form, "projects": projects})

# view list of projects
def view_projects(request):
  projects = Project.objects.all()
  return render(request, 'view-projects.html', {"title": "Proyectos", "projects": projects})

# view storages
def view_storages(request):
  storages = Storage.objects.all()
  return render(request, 'view-storages.html', {"title": "Ubicaciones", "storages": storages})