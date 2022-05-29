from django.contrib import admin
from .models import Categoria, Producto, Region, Comuna, Usuario, Rol, Direccion, Status

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Status)