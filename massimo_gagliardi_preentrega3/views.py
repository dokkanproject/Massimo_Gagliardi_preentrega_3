from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from massimo_gagliardi_preentrega3.models import Productos
from massimo_gagliardi_preentrega3.forms import crearFormulario, buscarFormulario

def inicio(request):
    return render(request, 'index.html')

def sobreMi(request):
    return render(request,'about.html')

def agregarProductos(request):
    
    formulario = crearFormulario()
    
    if request.method == 'POST':
        
        formulario = crearFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            prod = Productos(producto=data.get('producto'), precio=data.get('precio'), stock=data.get('stock'))
            prod.save()
            return redirect('buscar_producto')
    
    return render(request, 'add_product.html', {'form':formulario})

def buscarProductos(request):
    
    formulario  = buscarFormulario(request.GET)
    
    if formulario.is_valid():
        producto    = formulario.cleaned_data.get('producto')
        productos   = Productos.objects.filter(producto__icontains=producto)
    else:
        productos   = Productos.objects.all()
    
    return render(request, 'buscar_producto.html', {'productos': productos, 'form': formulario})