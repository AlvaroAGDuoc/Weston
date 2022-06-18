from django.urls import path
from rest_categoria.views import lista_categorias, control_categoria
from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_categorias/',lista_categorias,name='lista_categorias'),
    path('control_categoria/<codigo>', control_categoria, name = 'control_categoria'),
    path('login/',login,name="login"),
]