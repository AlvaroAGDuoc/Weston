from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Categoria, Producto, Region, Comuna, Cliente
# Create your views here.

def inicio(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {"reg": regiones, "com": comunas}
    return render(request, 'app/registro.html', contexto)

def enviar_registro(request):
    nombre = request.POST['nombre']
    email = request.POST['email']
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    celu = request.POST['telefono']
    contrasena = request.POST['contrasena']

    com2 = Comuna.objects.get(idComuna = comuna)
    Cliente.objects.create(nombre=nombre, email=email, direccion=direccion, comuna=com2, telefono=celu, clave=contrasena)
    return redirect('registro')

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
    return render(request, 'app/perfil_usuario.html')

def editar_usuario(request):
    return render(request, 'app/editar_usuario.html')

def cambiar_contrasena(request):
    return render(request, 'app/cambiar_contrasena.html')

def menu_admin(request):
    return render(request, 'app/admin.html')

def form_agregar(request):
    categorias = Categoria.objects.all()
    contexto = {"cat": categorias}
    return render(request, 'app/agregar_producto.html', contexto)

def registrar_p(request):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    imagen = request.FILES['foto']
    categoria = request.POST['categoria']
    stock = request.POST['stock']
    descripcion = request.POST['descripcion']

    cat2 = Categoria.objects.get(idCategoria = categoria)
    Producto.objects.create(nombre=nombre, precio= precio, imagen= imagen, categoria= cat2, stock= stock, descripcion = descripcion)
    return redirect('form_agregar')

def lista_usuarios(request):
    return render(request, 'app/lista_usuarios.html')

def modificar_producto(request):
    return render(request, 'app/modificar_producto.html')

def registro_ventas(request):
    return render(request, 'app/registro_ventas.html')



    