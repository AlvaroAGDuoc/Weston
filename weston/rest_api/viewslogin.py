import email
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from app.models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    correo = data['email']
    clave = data['password']
    try:
        user1 = Usuario.objects.get(email = correo)
    except Usuario.DoesNotExist:
        return Response("Usuario Incorrecto")

    pass_valida = check_password(clave, user1.password)

    if not pass_valida:
        return Response("Contraseña Incorrecta")
    
    token, created = Token.objects.get_or_create(user = user1)
    return Response(token.key)