
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.
class AdministradorUsuarios(BaseUserManager):
    def create_user(self, email, nombre, telefono,direccion, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Los usuarios deben tener un correo electronico")
        if not password:
            raise ValueError("Los usuarios deben tener una contraseña")
        if not nombre:
            raise ValueError("Los usuarios deben tener un nombre")
        objeto_usuario = self.model(
            email = self.normalize_email(email),
            nombre = nombre,
            telefono = telefono,
            direccion = direccion,
        )
        objeto_usuario.set_password(password) # cambiar contraseña usuario
        objeto_usuario.staff = is_staff
        objeto_usuario.admin = is_admin
        objeto_usuario.activo = is_active
        
        objeto_usuario.save(using=self._db)
        return objeto_usuario

    def create_staffuser(self, email, nombre, telefono, direccion,  password=None):
        usuario = self.create_user(
            email,
            nombre=nombre,
            telefono = telefono,
            direccion = direccion,
            password=password,
            is_staff=True
            
        )
        
        return usuario

    def create_superuser(self, email, nombre, telefono, direccion,  password=None):
        usuario = self.create_user(
            email,
            nombre=nombre,
            telefono = telefono,
            direccion = direccion,
            password=password,
            is_staff=True,
            is_admin=True
            
        )
        
        return usuario

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True, verbose_name="Id de la region")
    nombre =  models.CharField(max_length=30, verbose_name="Nombre de la region",null=True, blank=False)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name="Id de la comuna")
    nombre =  models.CharField(max_length=30, verbose_name="Nombre de la comuna",null=True, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True, verbose_name="Id de rol")
    descripcion = models.CharField(max_length=40, verbose_name="Nombre de la direccion",null=True, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
   
    def __str__(self):
         return self.descripcion

class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='Correo electronico', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre completo', max_length=40, blank=True, null=True)
    telefono = models.IntegerField(verbose_name="Telefono del usuario", null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    active = models.BooleanField(default=True) # puede conectarse
    staff = models.BooleanField(default=False) # un usuario admin; no super-usuario
    admin = models.BooleanField(default=False) # un super-usuario

     # observa la ausencia de un "Password field", que está integrado

    USERNAME_FIELD = 'email' # Con que se logeara
    REQUIRED_FIELDS = ['nombre', 'telefono'] # Email & Contraseña son requeridas por DEFAULT.

    objects = AdministradorUsuarios()

    def __str__(self):
        return self.email

    def get_nombre(self): #obtener nombre

        return self.nombre

    def has_perm(self, perm, obj=None):
        "El usuario tiene un permiso en especifico?"
        # Posible respuesta simple: Si, siempre
        return True

    def has_module_perms(self, app_label):
        "El usuario tiene permiso para ver la aplicacion?"
        # Posible respuesta simple: Si, siempre
        return True


    @property
    def is_staff(self):
        "Es el usuario un miembro de staff?"
        return self.staff

    @property
    def is_admin(self):
        "Es el usuario un miembro admin?"
        return self.admin

    @property
    def is_active(self):
        "Es el usuario un miembro activo?"
        return self.active

class Categoria(models.Model):
    idCategoria =  models.AutoField(primary_key=True, verbose_name="Id de la categoria")
    nombre = models.CharField(max_length=15, verbose_name="Nombre de la categoria",null=True, blank=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id del producto")
    nombre = models.CharField(max_length=40, verbose_name="Nombre del producto",null=True, blank=False)
    precio = models.IntegerField(verbose_name="Precio del producto", null=True, blank= False)
    imagen = models.ImageField(upload_to="productos", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name="Stock del producto", null=True, blank= False)
    descripcionCorta = models.TextField(null=True, blank= False, verbose_name="Descripcion corta del producto")
    descripcion = models.TextField(null=True, blank= False, verbose_name="Descripcion del producto")

    def __str__(self):
        return self.nombre



class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_compra = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la compra")
    completada = models.BooleanField(default=False, null=True, blank=False)
    transaccion_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class Detalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0,null=True, blank=True, verbose_name="Cantidad del detalle")
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idDetalle