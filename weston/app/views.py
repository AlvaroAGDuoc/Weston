from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    return render(request, 'app/registro.html')

def producto_cocina(request):
    return render(request, 'app/producto_cocina.html')

def producto_libreros(request):
    return render(request, 'app/producto_libreros.html')

def producto_muebles(request):
    return render(request, 'app/producto_muebles.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def contrasena_olvidada(request):
    return render(request, 'app/contrasena_olvidada.html')

def carrito(request):
    return render(request, 'app/carrito_compras.html')

def muestra_producto(request):
    return render(request, 'app/muestra_producto.html')

def perfil(request):
    return render(request, 'app/vista_usuario/perfil_usuario.html')

def editar_usuario(request):
    return render(request, 'app/vista_usuario/editar_usuario.html')

def cambiar_contrasena(request):
    return render(request, 'app/vista_usuario/cambiar_contrasena.html')

def menu_admin(request):
    return render(request, 'app/vista_admin/admin.html')

def agregar_producto(request):
    return render(request, 'app/vista_admin/agregar_producto.html')

def lista_usuarios(request):
    return render(request, 'app/vista_admin/lista_usuarios.html')

def modificar_producto(request):
    return render(request, 'app/vista_admin/modificar_producto.html')

def registro_ventas(request):
    return render(request, 'app/vista_admin/registro_ventas.html')



    