from rest_framework import serializers
from app.models import Producto, Categoria, Region

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre','precio','imagen','categoria','stock','descripcionCorta','descripcion']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['nombre']
