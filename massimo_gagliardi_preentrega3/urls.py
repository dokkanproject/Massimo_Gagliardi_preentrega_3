from django.urls import path
from massimo_gagliardi_preentrega3.views import inicio, agregarProductos, buscarProductos

urlpatterns = [
    path('', inicio),
    path('add_product/',agregarProductos),
    path('search_product/', buscarProductos)
]
