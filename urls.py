from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('ordens/', include('ordens.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('configuracoes/', include('configuracoes.urls')),
] 