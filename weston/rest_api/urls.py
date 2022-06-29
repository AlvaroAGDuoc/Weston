from django.urls import path
from .views import lista_productos, control_producto, lista_categorias, control_categoria, lista_regiones, control_region
from .viewslogin import login

urlpatterns = [
    path('lista_productos/',lista_productos,name='lista_productos'),
    path('control_producto/<codigo>', control_producto, name = 'control_producto'),
    path('lista_categorias/',lista_categorias,name='lista_categorias'),
    path('control_categoria/<codigo>', control_categoria, name = 'control_categoria'),
    path('lista_regiones/',lista_regiones,name='lista_region'),
    path('control_region/<codigo>', control_region, name = 'control_region'),
    path('login/',login,name="login"),
]