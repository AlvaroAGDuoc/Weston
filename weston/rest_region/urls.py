from django.urls import path
from rest_region.views import lista_region, control_region
from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_region/',lista_region,name='lista_region'),
    path('control_region/<codigo>', control_region, name = 'control_region'),
    path('login/',login,name="login"),
]