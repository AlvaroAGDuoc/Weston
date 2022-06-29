from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductoSerializer, CategoriaSerializer, RegionSerializer
from app.models import Producto, Categoria, Region

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt

# Api de productos

@api_view(['GET', 'POST'])  # LISTA PRODUCTOS
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  # PRODUCTO
@permission_classes((IsAuthenticated,))
def control_producto(request, codigo):
    #Para controlar
    try:
        p = Producto.objects.get(idProducto=codigo)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(p)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(p,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# *****************************************************************************************

# Api de categorias

@api_view(['GET', 'POST'])  # LISTA CATEGORIA
@permission_classes((IsAuthenticated,))
def lista_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  # PRODUCTO
@permission_classes((IsAuthenticated,))
def control_categoria(request, codigo):
    #Para controlar
    try:
        c = Categoria.objects.get(idCategoria=codigo)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(c)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = CategoriaSerializer(c,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        c.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# *****************************************************************************************

# Api de regiones

@api_view(['GET', 'POST'])  # LISTA REGION
@permission_classes((IsAuthenticated,))
def lista_regiones(request):
    if request.method == 'GET':
        regiones = Region.objects.all()
        serializer = RegionSerializer(regiones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = RegionSerializer(data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])  # PRODUCTO
@permission_classes((IsAuthenticated,))
def control_region(request, codigo):
    #Para controlar
    try:
        r = Region.objects.get(idRegion=codigo)
    except Region.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RegionSerializer(r)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = RegionSerializer(r,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        r.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)