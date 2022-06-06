from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria, Detalle, Producto, Region, Direccion, Usuario, Compra
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import RegistroUsuario
from django.contrib.auth import authenticate, login
import datetime
# Create your views here.

def registro(request):
    data = {
        'form': RegistroUsuario()
    }

    if request.method == 'POST':
        formulario = RegistroUsuario(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(email=formulario.cleaned_data['email'],
            password = formulario.cleaned_data['password1'])
            login(request, usuario)
            return redirect(to="inicio")
        data["form"] = formulario
   
    return render(request, 'registration/registro.html', data)

def carrito(request):

    if request.user.is_authenticated:
        usuario = request.user
        compra, created = Compra.objects.get_or_create(usuario=usuario, completada=False)
        productos = compra.detalle_set.all()
        productosCarrito = compra.obtener_productos_carrito
    else:
        productos = []
        compra = {"obtener_total_carrito": 0, 'obtener_productos_carrito': 0}
    context = {'productos':productos , 'compra': compra, 'productosCarrito': productosCarrito}
    
    return render(request, 'app/carrito_compras.html', context)


def checkout(request):

    if request.user.is_authenticated:
        usuario = request.user
        compra, created = Compra.objects.get_or_create(usuario=usuario, completada=False)
        productos = compra.detalle_set.all()
        productosCarrito = compra.obtener_productos_carrito
    else:
        productos = []
        compra = {"obtener_total_carrito": 0, 'obtener_productos_carrito': 0}
        
    context = {'productos':productos , 'compra': compra, 'productosCarrito': productosCarrito}
    return render(request, 'app/checkout.html', context)

def actualizarProducto(request):
    data = json.loads(request.body)
    productoId = data['productoId']
    action = data['action']

    print('Action:', action)
    print('productoId:', productoId)   

    usuario = request.user
    producto = Producto.objects.get(idProducto=productoId)
    compra,created = Compra.objects.get_or_create(usuario=usuario, completada = False)
    detalle, created = Detalle.objects.get_or_create(compra=compra, producto=producto)

    if action == 'add':
        detalle.cantidad = (detalle.cantidad + 1)
    elif action == 'remove':
        detalle.cantidad = (detalle.cantidad - 1)

    detalle.save()

    if detalle.cantidad <= 0:
        detalle.delete()
    return JsonResponse('El producto ha sido agregado', safe=False)

def muestra_producto(request, id):
    if request.user.is_authenticated:
        usuario = request.user
        compra, created = Compra.objects.get_or_create(usuario=usuario, completada=False)
        productos = compra.detalle_set.all()
        productosCarrito = compra.obtener_productos_carrito
    else:
        productos = []
        compra = {"obtener_total_carrito": 0, 'obtener_productos_carrito': 0}
        productosCarrito = compra['obtener_productos_carrito']


    producto = Producto.objects.get(idProducto = id)
    contexto = {
        "producto": producto,
        'productos': productos,
        "productosCarrito": productosCarrito
    }

    return render(request, 'app/muestra_producto.html', contexto)

def procesarCompra(request):
    transaccion_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        usuario = request.user

    else:
        print("El usuario no esta logeado")
    return JsonResponse('Compra realizada', safe=False)
 
def inicio(request):
    productoInicio = Producto.objects.filter(stock__gte = 1, precio__lte = 5000)
    paginator = Paginator(productoInicio, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)

    contexto = {
        "productos": productos,
        'paginator': paginator,
    }
    return render(request, 'app/index.html', contexto)

def producto_cocina(request):
    productoCocina = Producto.objects.filter(categoria='1', stock__gte = 1)
    paginator = Paginator(productoCocina, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)


    contexto = {
        "productos": productos,
        'paginator': paginator
    }

    return render(request, 'app/producto_cocina.html', contexto)

def producto_libreros(request):
    productoLibreros = Producto.objects.filter(categoria='3', stock__gte = 1)
    paginator = Paginator(productoLibreros, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)

    contexto = {
        "productos": productos,
        'paginator': paginator
    }
    return render(request, 'app/producto_libreros.html', contexto)

def producto_muebles(request):
    productoMuebles = Producto.objects.filter(categoria='2', stock__gte = 1)
    paginator = Paginator(productoMuebles, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)

    contexto = {
        "productos": productos,
        'paginator': paginator
    }
    return render(request, 'app/producto_muebles.html', contexto)

def contacto(request):
    return render(request, 'app/contacto.html')

def contrasena_olvidada(request):
    return render(request, 'app/contrasena_olvidada.html')


def perfil(request):
    return render(request, 'app/perfil_usuario.html')

def editar_usuario(request):
    return render(request, 'app/editar_usuario.html')



def cambiar_contrasena(request):
    return render(request, 'app/cambiar_contrasena.html')

def menu_admin(request):
    producto = Producto.objects.all()
    contexto = {"productos": producto,}
    return render(request, 'app/admin.html',contexto)

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
    descripcionCorta = request.POST['descripcionCorta']
    descripcion = request.POST['descripcion']    

    cat2 = Categoria.objects.get(idCategoria = categoria)
    Producto.objects.create(nombre=nombre, precio= precio, imagen= imagen, categoria= cat2, stock= stock, descripcionCorta = descripcionCorta, descripcion = descripcion)
    return redirect('form_agregar')


def lista_usuarios(request):
    usuariosWeb = Usuario.objects.all()
    direccionUsuario = Direccion.objects.all()
    region = Region.objects.all()
    contexto = {
        "usuarios": usuariosWeb,
        "direccion": direccionUsuario,
        "region": region,
    }
    return render(request, 'app/lista_usuarios.html', contexto)

def modificar_producto(request, id):
    producto1 = Producto.objects.get(idProducto = id) # obtengo los datos del producto
    cat1 = Categoria.objects.all() # obtener todas las categorias para llenar combobox

    contexto =  {
        "producto" : producto1,
        "categoria" : cat1
    }

    return render(request, 'app/modificar_producto.html',contexto)

def modificar_p(request):
    idP = request.POST['idP']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    categoria = request.POST['categoria']
    stock = request.POST['stock']
    descripcionCorta = request.POST['descripcionCorta']
    descripcion = request.POST['descripcion']
    
    try:
        imagen = request.FILES['foto']
        cat2 = Categoria.objects.get(idCategoria = categoria)

        producto = Producto.objects.get(idProducto = idP) #el registro original
        #comienzo a reemplazar los valores en ese registro original
        producto.nombre = nombre
        producto.precio = precio
        producto.imagen = imagen
        producto.categoria = cat2
        producto.stock = stock
        producto.descripcionCorta = descripcionCorta
        producto.descripcion = descripcion
        
        categoria_p2 = Categoria.objects.get(idCategoria = categoria)

        producto.categoria = categoria_p2
        producto.save()
    except:
        cat2 = Categoria.objects.get(idCategoria = categoria)

        producto = Producto.objects.get(idProducto = idP) #el registro original
        #comienzo a reemplazar los valores en ese registro original
        producto.nombre = nombre
        producto.precio = precio
    
        producto.categoria = cat2
        producto.stock = stock
        producto.descripcionCorta = descripcionCorta
        producto.descripcion = descripcion

        categoria_p2 = Categoria.objects.get(idCategoria = categoria)

        producto.categoria = categoria_p2
        producto.save() 

    messages.success(request, 'Producto Modificado')
    return redirect('menu_admin')

def eliminar_producto(request, id):
    producto1 = Producto.objects.get(idProducto = id)
    producto1.delete()
    messages.success(request, 'Producto eliminado')

    return redirect('menu_admin')
    
def registro_ventas(request):
    return render(request, 'app/registro_ventas.html')



    