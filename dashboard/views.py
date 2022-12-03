from django.shortcuts import render

def index(request):
  return render(request, 'dashboard.html', {"title": "Buscar Producto"})

def settings(request):
  return render(request, 'settings.html', {"title": "Configuración"})

def add(request):
  return render(request, 'add.html', {"title": "Agregar Producto"})
