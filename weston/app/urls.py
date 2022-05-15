from django.urls import path
from .views import inicio, login, registro, producto_cocina, producto_libreros, producto_muebles, contacto, contrasena_olvidada, carrito, muestra_producto, perfil, editar_usuario, cambiar_contrasena, menu_admin, agregar_producto, lista_usuarios, modificar_producto, registro_ventas

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('cocina/', producto_cocina, name="cocina"),
    path('libreros/', producto_libreros, name="libreros"),
    path('muebles/', producto_muebles, name="muebles"),
    path('contacto/', contacto, name="contacto"),
    path('carrito/', carrito, name="carrito"),
    path('muestra_producto/', muestra_producto, name="muestra_producto"),
    path('perfil/', perfil, name="perfil"),
    path('editar_perfil/', editar_usuario, name="editar_perfil"),
    path('cambiar_contrasena/', cambiar_contrasena, name="cambiar_contrasena"),
    path('menu_admin/', menu_admin, name="menu_admin"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('modificar_producto/', modificar_producto, name="modificar_producto"),
    path('ventas/', registro_ventas, name="registro_ventas"),
]