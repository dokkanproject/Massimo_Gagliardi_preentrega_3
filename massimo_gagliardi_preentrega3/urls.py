from django.urls import path
from massimo_gagliardi_preentrega3.views import inicio, agregarProductos, buscarProductos, sobreMi

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', sobreMi, name='sobreMi'),
    path('add_product/',agregarProductos, name='agregar_producto'),
    path('buscar_producto/', buscarProductos, name='buscar_producto')
]
