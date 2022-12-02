from django.shortcuts import render


def index(request):
  return render(request, 'search_product.html', {"title": "Buscar Producto"})