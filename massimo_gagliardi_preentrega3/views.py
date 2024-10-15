from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from massimo_gagliardi_preentrega3.models import Producto

def inicio(request):
    return render(request, 'index.html')

def agregarProductos(request):
    return HttpResponse("Agregar un Producto")

def buscarProductos(request):
    return HttpResponse("Buscar un Producto")