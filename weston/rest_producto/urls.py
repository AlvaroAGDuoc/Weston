from django.urls import path
from rest_producto.views import lista_productos, control_producto
from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_productos/',lista_productos,name='lista_productos'),
    path('control_producto/<codigo>', control_producto, name = 'control_producto'),
    path('login/',login,name="login"),
]