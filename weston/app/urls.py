from django.urls import path

from .views import inicio, login ,  registro, modificar_p, producto_cocina, producto_libreros, producto_muebles, contacto, eliminar_producto, carrito, muestra_producto, perfil, form_agregar, editar_usuario, cambiar_contrasena, menu_admin, registrar_p, lista_usuarios, modificar_producto, registro_ventas, enviar_registro

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login ,name="login"),
    path('registro/', registro, name="registro"),
    path('enviar_registro/', enviar_registro, name="enviar_registro"),
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
    path('form_agregar/', form_agregar, name="form_agregar"),
    path('registrar_p/', registrar_p, name="registrar_p"),
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('modificar_producto/<int:id>', modificar_producto, name="modificar_producto"),
    path('modificar_p/', modificar_p, name="modificar_p"),
    path('eliminar_producto/<int:id>', eliminar_producto, name="eliminar_producto"),
    path('ventas/', registro_ventas, name="registro_ventas"),
]