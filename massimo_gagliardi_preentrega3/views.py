from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from massimo_gagliardi_preentrega3.models import Producto

def inicio(request):
    return render(request, 'index.html')

def sobreMi(request):
    return render(request,'about.html')

def agregarProductos(request, prod, precio, stock):
    
    prod = Producto(producto=prod, precio=precio, stock=stock)
    prod.save()
    
    return render(request, 'add_product.html', {'producto':prod})

def buscarProductos(request):
    
    return render(request, 'buscar_producto.html', {'producto':''})