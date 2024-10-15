from django.urls import path
from massimo_gagliardi_preentrega3.views import agregarProductos, buscarProductos

urlpatterns = [
    path('add_product/',agregarProductos),
    path('search_product/', buscarProductos)
]
