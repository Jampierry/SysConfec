from django.urls import path
from .views import cadastro_usuario

urlpatterns = [
    path('novo/', cadastro_usuario, name='cadastro_usuario'),
] 