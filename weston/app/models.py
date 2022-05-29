from django.db import models

# Create your models here.
class Status(models.Model):
    idStatus = models.AutoField(primary_key=True, verbose_name="Id de status")
    nombre =  models.CharField(max_length=30, verbose_name="Nombre del status",null=True, blank=False)

    def __str__(self):
        return self.nombre

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
    descripcion = models.TextField(null=True, blank= False, verbose_name="Descripcion del producto")
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True, verbose_name="Id de rol")
    nombre = models.CharField(max_length=40, verbose_name="Nombre tipo rol",null=True, blank=False)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Id del usuario")
    nombre =  models.CharField(max_length=40, verbose_name="Nombre del usuario",null=True, blank=False)
    email =  models.EmailField(max_length=50, verbose_name="Email del usuario", unique=True)
    clave = models.CharField(max_length=30, verbose_name="Clave del usuario", null=True, blank=False)
    telefono = models.IntegerField(verbose_name="Telefono del usuario")
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
         return self.descripcion



# class Compra(models.Model):
#     idCompra = models.AutoField(primary_key=True, verbose_name="Id de la compra")
#     fecha = models.DateField(verbose_name="Fecha de la compra")
#     total = models.IntegerField(verbose_name="Total de la compra")
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.idCompra

# class Detalle(models.Model):
#     idDetalle = models.AutoField(primary_key=True, verbose_name="Id del detalle")
#     cantidad = models.IntegerField(verbose_name="Cantidad del detalle")
#     subtotal = models.IntegerField(verbose_name="Subtotal del detalle")
#     compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

#     def __str__(self):
#         return self.idDetalle