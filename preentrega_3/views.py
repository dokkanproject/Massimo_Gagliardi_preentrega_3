from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from massimo_gagliardi_preentrega3.models import Productos

def inicio(request):
    return render(request, 'index.html')

def sobreMi(request):
    return render(request,'about.html')

def agregarProductos(request):
    
    request.POST['producto']
    prod = Productos(producto=request.POST.get('producto'), precio=request.POST.get('precio'), stock=request.POST.get('stock'))
    prod.save()
    
    return render(request, 'add_product.html', {'producto':''})

def buscarProductos(request):
    
    return render(request, 'buscar_producto.html', {'producto':''})