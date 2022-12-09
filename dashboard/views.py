from django.shortcuts import render, redirect
from dashboard.models import Product
from dashboard.forms import ProductForm, CategoryForm
from django.contrib import messages

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
  return render(request, 'add.html', {"title": "Agregar Producto", "product_form": product_form, "products": products})

def add_category(request):
  if request.method == "POST":
    pass
  return render(request, 'add-category.html', {"title": "Agregar Categoría"})