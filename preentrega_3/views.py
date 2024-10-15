from django.http import HttpResponse

def agregarProductos(request):
    return HttpResponse("Agregar un Producto")

def buscarProductos(request):
    return HttpResponse("Buscar un Producto")