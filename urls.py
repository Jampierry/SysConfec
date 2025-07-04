from django.urls import path, include

urlpatterns = [
    path('funcionarios/', include('funcionarios.urls', namespace='funcionarios')),
] 