from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria, Detalle, Producto, Region, Direccion, Usuario, Compra, Comuna
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

import json
import datetime
from .forms import UserLoginForm, UserSignUpForm
# Create your views here.


def login_inicio(request):
    return render(request, 'registration/login.html')

def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('inicio')
        else:
            messages.warning(request, 'Correo Electrónico o Contraseña inválida')
            return redirect('login_inicio')

    messages.error(request, 'Formulario Inválido')
    return redirect('login_inicio')


def singup_view(request):
    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        nombre = signup_form.cleaned_data.get('nombre')
        telefono = signup_form.cleaned_data.get('telefono')
        password = signup_form.cleaned_data.get('password')
       
        try:
           
            user = Usuario.objects.create(
                email=email,
                nombre=nombre,
                telefono=telefono,
                password=make_password(password),
            )
            login(request, user)
            return redirect('inicio')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})
    return render(request, 'registration/registro.html')


def logout_view(request):
    logout(request)
    return redirect('inicio')





def perfil(request):
    usuario = request.user
    existe =  Direccion.objects.filter(usuario = usuario).exists()

    if existe:
        direccion = Direccion.objects.get(usuario = usuario)
        direccion = direccion.descripcion
    else:
        direccion = "No tiene ninguna direccion"
    
    contexto = {
        "direccion" : direccion
    }    
    return render(request, 'app/perfil_usuario.html',contexto) 

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

    region = Region.objects.all()
    comuna = Comuna.objects.all()

    if request.user.is_authenticated:
        usuario = request.user
        compra, created = Compra.objects.get_or_create(usuario=usuario, completada=False)
        productos = compra.detalle_set.all()
        productosCarrito = compra.obtener_productos_carrito
    else:
        productos = []
        compra = {"obtener_total_carrito": 0, 'obtener_productos_carrito': 0}
        
    context = {'productos':productos , 'compra': compra, 'productosCarrito': productosCarrito, 'region': region, 'comuna':comuna}
    return render(request, 'app/checkout.html', context)

def actualizarProducto(request):
    data = json.loads(request.body)
    productoId = data['productoId']
    action = data['action']

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
    data = json.loads(request.body)

    if request.user.is_authenticated:
        usuario = request.user
        compra, created = Compra.objects.get_or_create(usuario=usuario, completada=False)
        total = data['form']['total']
        compra.transaccion_id = transaccion_id

        
        compra.completada = True
        compra.save()


        com = data['envio']['comuna']
        com2 = Comuna.objects.get(idComuna = com)


        Direccion.objects.create(
            descripcion = data['envio']['direccion'],
            comuna = com2,
            usuario = usuario,
            compra = compra
        )

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
    

def editar_usuario(request):
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    usuario = request.user
    existe =  Direccion.objects.filter(usuario = usuario).exists()

    if existe:
        direccion = Direccion.objects.get(usuario = usuario)
        direccion = direccion.descripcion
    else:
        direccion = ""
    
    contexto = {
        "direccion" : direccion, 'region': region, 'comuna':comuna
    }
    return render(request, 'app/editar_usuario.html',contexto)

def post_editar_usuario(request):
    usuario = request.user
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    telefono = request.POST['contacto']

    existe =  Direccion.objects.filter(usuario = usuario).exists()
    com = Comuna.objects.get(idComuna = comuna)

    if existe:
        direccion2 = Direccion.objects.get(usuario = usuario)
        direccion2.descripcion = direccion 
        direccion2.comuna = com
        direccion2.save()
    else:
        direccion2 = Direccion.objects.create(descripcion = direccion, comuna= com, usuario=usuario)
        direccion2.save()
    
    usuario.telefono = telefono  

    usuario.save()
    return redirect('perfil')


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
    usuario = Usuario.objects.all()
    direccion = Direccion.objects.all()
    region = Region.objects.all()
    contexto = {
        "usuarios": usuario,
        "direccion": direccion,
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



    