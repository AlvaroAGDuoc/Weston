from django.shortcuts import render, redirect
from .models import Categoria, Producto, Region, Comuna, Rol, Usuario, Direccion, Status
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def inicio(request):
    productoInicio = Producto.objects.filter(stock__gte = 1, status = '3', precio__lte = 5000)
    paginator = Paginator(productoInicio, 1)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)

    contexto = {
        "productos": productos,
        'paginator': paginator
    }
    return render(request, 'app/index.html', contexto)


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
    rol = 1

    com2 = Comuna.objects.get(idComuna = comuna)
    rol2 = Rol.objects.get(idRol = rol)  

    Usuario.objects.create(nombre=nombre, email=email, clave=contrasena, telefono=celu, rol=rol2)

    usuarioNuevo = Usuario.objects.get(email = email)

    Direccion.objects.create(descripcion=direccion, comuna=com2, usuario= usuarioNuevo) 
    return redirect('login')

def producto_cocina(request):
    productoCocina = Producto.objects.filter(categoria='3', stock__gte = 1, status = '3')
    paginator = Paginator(productoCocina, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)


    contexto = {
        "productos": productos,
        'paginator': paginator
    }

    return render(request, 'app/producto_cocina.html', contexto)

def producto_libreros(request):
    productoLibreros = Producto.objects.filter(categoria='2', stock__gte = 1, status = '3')
    paginator = Paginator(productoLibreros, 6)

    page = request.GET.get("page") or 1   
    productos = paginator.get_page(page)

    contexto = {
        "productos": productos,
        'paginator': paginator
    }
    return render(request, 'app/producto_libreros.html', contexto)

def producto_muebles(request):
    productoMuebles = Producto.objects.filter(categoria='1', stock__gte = 1, status = '3')
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

def carrito(request):
    return render(request, 'app/carrito_compras.html')


def perfil(request):
    return render(request, 'app/perfil_usuario.html')

def editar_usuario(request):
    return render(request, 'app/editar_usuario.html')

def muestra_producto(request, id):
    producto = Producto.objects.get(idProducto = id)

    contexto = {
        "producto": producto
    }

    return render(request, 'app/muestra_producto.html', contexto)

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
    
    status = 3

    cat2 = Categoria.objects.get(idCategoria = categoria)
    status2 = Status.objects.get(idStatus = status)
    Producto.objects.create(nombre=nombre, precio= precio, imagen= imagen, categoria= cat2, stock= stock, descripcionCorta = descripcionCorta, descripcion = descripcion,  status = status2)
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



    